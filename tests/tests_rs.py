from rs import encode, decode, encode_textbook, syndrome
from gf import exfield_gen
import random

def test_rs_noiseless_channel():
    field = exfield_gen(4, 0b11001)
    a = field[0]
    n, k, t =15, 9, 2
    b =[a[0], a[5], a[10]]
    gen = [b[0], b[1], b[1], b[0], b[0], b[2], b[0]]
    u = [random.randrange(16) for _ in range(k)]
    codeword = encode(n, k, t, u =u, gen=gen, field=field)                                # (14, 0, 14, 0, 6, 8, 6, 8, 0, 0, ...)
    decoded, error_locations, error_values = decode(n, k, t, r=codeword, field=field)

    assert u == decoded, print( f'{u} -> {codeword} -> {decoded}', error_locations, error_values, sep ='\n')

def test_rs_noisy_channel():
    field = exfield_gen(4, 0b11001)
    a = field[0]
    n, k, t =15, 9, 2
    b =[a[0], a[5], a[10]]
    gen = [b[0], b[1], b[1], b[0], b[0], b[2], b[0]]
    u = [b[0], b[1], b[0], 0, 0, 0, 0, 0, 0]
    codeword = encode(n, k, t, u =u, gen=gen, field=field)                                # (14, 0, 14, 0, 6, 8, 6, 8, 0, 0, ...)
    codeword[-1] =b[0]  # b[0] = a[0] = 8
    codeword[-2] =b[1]  # b[1] = a[5] = 6
    # codeword[-3] =a[4]

    decoded, error_locations, error_values = decode(n, k, t, r=codeword, field=field)
    print(error_values, error_locations)
    assert u == decoded, print( f'{u} -> {codeword} -> {decoded}', error_locations, error_values, sep ='\n')

test_rs_noiseless_channel()
test_rs_noisy_channel()