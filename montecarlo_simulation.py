import random, csv
import cir
import crc
import bch
import rs
import gf
import channel

random.seed(1337)


def bit_count(x: int) -> int:
    return int(x).bit_count()

def payload_errors(decoded_payload: int, original_payload: int, k: int) -> int:
    mask = (1 << k) - 1
    return bit_count((decoded_payload & mask) ^ (original_payload & mask))

def crc_sim(EbN0_db: float, n: int = 7, 
            k: int = 4, g: int = 0b1101, frames: int = 1000):
    """Cyclic code error-correcting using error traping. (corrects just one bit if there is more decoder fails)"""
    EbN0 = 10 ** (EbN0_db / 10.0)
    frame_errors = 0
    total_bits = 0

    for _ in range(frames):
        u = random.getrandbits(k)
        codeword = crc.encode(n, k, u=u, g=g)

        received_codeword = 0
        for idx in range(n):
            b =(codeword >> idx) & 1
            r =channel.AWGN(EbN0, b)
            received_codeword |= (r & 1) << idx

        syndrome = crc.syndrome(n, k, received_codeword, g)
        packet_payload = received_codeword
        frame_errors += payload_errors(packet_payload, u, k)
        total_bits += k
        if frame_errors >= 100:
            break

    return frame_errors / total_bits if total_bits else 0.0, frame_errors, total_bits

def bch_sim(EbN0_db: float, m =4,
            n = 15, k = 7, t = 2, 
            g = 0b100010111, frames = 1000):
    """BCH binary.code Monte Carlo using the CRC encoder."""
    if (n, m) == (15, 4):
        field = gf.exfield_gen(m, 0b11001)
    
    EbN0 = 10 ** (EbN0_db / 10.0)

    frame_errors = 0
    total_bits = 0

    for _ in range(frames):
        u = random.getrandbits(k)
        codeword = bch.encode(n, k, u=u, g=g)

        received_codeword =0
        for idx in range(n):
            b= (codeword >> idx) & 1
            r = channel.AWGN(EbN0, b)
            received_codeword |= (r & 1) << idx

        decoded, _, _ = bch.decode(n, k, t, received_codeword, field)

        frame_errors += payload_errors(decoded, u, k)
        total_bits += k
        if(frame_errors >= 100):
            break

    return frame_errors / total_bits if total_bits else 0.0, frame_errors, total_bits

def rs_symbol_errors(decoded_payload: list, original_payload: list):
    return sum(1 for a, b in zip(decoded_payload, original_payload) if a != b)

def rs_bits_errors(decoded_payload :list, original_payload :list):
    return sum(bit_count(a ^ b) for a, b in zip(decoded_payload, original_payload) if a != b)

def rs_sim(EbN0_db: float, field =(),q =4, m =2,
           n: int = 15, k: int = 9, t: int = 2, 
           gen :list = [], frames: int = 1000):
    """RS/non-binary BCH-like simulation using GF(16) symbols.
    """
    if (n, k, t, gen) == (15, 9, 2, []):
        field = gf.exfield_gen(4, 0b11001)
        qm = 16
        a =field[0]
        b =[a[0], a[5], a[10]]
        gen =[b[0], b[1], b[1], b[0], b[0], b[2], b[0]]
    elif(gen == []):
        raise ValueError('generator error: provide a generator.')
    else:
        raise ValueError('code parameters are not provided.')

    EbN0 = 10 ** (EbN0_db / 10.0)

    frame_error = 0
    total_bits = 0

    for _ in range(frames):
        u = [random.randrange(0, q**m) for _ in range(k)]
        codeword = rs.encode(n, k, t, u=u, gen=gen, field=field)
        received_symbols = []

        # send symbols (map them to bits)
        for symbol in codeword:
            r = [channel.AWGN(EbN0, stream) for stream in cir.sym2bits(q, symbol)]
            received_symbols.append(cir.bits2sym(r))

        # decode received symbols:
        decoded_symbols, _, _ = rs.decode(n, k, t, r=received_symbols, field=field)
        
        frame_error +=rs_bits_errors(decoded_symbols, u)
        total_bits += (k*q)
        if (frame_error >= 100):
            break

    BER = frame_error / total_bits
    return BER, frame_error, total_bits

def main():
    SNRs = [i/10 for i in range(-100, 101, 5)]
    results =[]
    for ebn0 in SNRs:
        ber, bit_err, total_bit = crc_sim(ebn0, frames=5000)
        results.append((ebn0, ber, bit_err, total_bit))
    with open("./SIM_FILES/crc_ber.csv", 'w', newline='') as f:
        fwriter = csv.writer(f)
        fwriter.writerow(["EbN0", "BER", "total error", "total bits"])
        fwriter.writerows(results)

    results =[]
    for ebn0 in SNRs:
        ber, bit_err, total_bit = bch_sim(ebn0, frames=5000)
        results.append((ebn0, ber, bit_err, total_bit))
    with open("./SIM_FILES/bch_ber.csv", 'w', newline='') as f:
        fwriter = csv.writer(f)
        fwriter.writerow(["EbN0", "BER", "total error", "total bits"])
        fwriter.writerows(results)

    results =[]
    for ebn0 in SNRs:
        ber, bit_err, total_bit = rs_sim(ebn0, frames=1000)
        results.append((ebn0, ber, bit_err, total_bit))
    with open("./SIM_FILES/rs_ber.csv", 'w', newline='') as f:
        fwriter = csv.writer(f)
        fwriter.writerow(["EbN0", "BER", "total error", "total bits"])
        fwriter.writerows(results)

if __name__ == '__main__':
    main()
