from bch import encode, decode
from gf import exfield_gen
import random as rnd

rnd.seed(3337)

f16 = exfield_gen(4, 0b11001)
a = f16[0]

def noiseless_test():
    u = 0b10000
    codeword = encode(15, 5, u =u, g =0b11101100101) # (15, 5) triple error correction: t =3
    decoded = decode(15, 5, 3, r =codeword, field =f16)
    assert decoded == u, print(bin(codeword), ' --> ', bin(decoded), ' u= ', bin(u))

def noisy_test():
    u = 0b10000
    codeword = encode(15, 5, u =u, g =0b11101100101) # (15, 5) triple error correction: t =3
    codeword ^= (1<<2)
    codeword ^= (1<<5)
    codeword ^= (1<<7)
    decoded = decode(15, 5, 3, r =codeword, field =f16)
    assert decoded == u, print(bin(codeword), ' --> ', bin(decoded), ' u= ', bin(u))

noiseless_test()
noisy_test()
# r =decode(15, 5, 3, r =0b000101000000100, field =f16)
# print(r)