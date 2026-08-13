from channel import AWGN
from cir import sym2bits, bits2sym
import random as rnd

u = rnd.randrange(0, 2**64)

u_star = [AWGN(25, bit) for bit in sym2bits(64, u)]


def b2s(k, b):
    s =0
    for i, bb in zip(range(k), b):
        s += (bb << i)

    return s

u_sta = b2s(64, u_star)

# print(bin(u), bin(u_sta), (u ^ u_sta).bit_count(), sep ='\n')

for EbN0_db in [-10, -5, 0, 5, 10]:
    EbN0 = 10 ** (EbN0_db / 10)

    errors = 0
    total = 100000

    for _ in range(total):
        b = rnd.randrange(2)
        bhat = AWGN(EbN0, b)

        if b != bhat:
            errors += 1

    print(EbN0_db, errors / total)
