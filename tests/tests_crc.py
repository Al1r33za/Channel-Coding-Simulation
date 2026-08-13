from crc import encode, decode
from gf import exfield_gen
import random as rnd

rnd.seed(89)

def noiseless_test():
    u =rnd.randrange(16)
    codeword = encode(7, 4, u, 0b1101)
    decoded, _, _ = decode(7, 4, r =codeword, g =0b1101)
    assert decoded == u, print(u, '->', codeword, '->', decoded)

def noisy_test():
    u =rnd.randrange(16)
    codeword = encode(7, 4, u, 0b1101)
    codeword ^= (1<<5)
    decoded, _, _ = decode(7, 4, r =codeword, g =0b1101)
    assert decoded == u, print(u, '->', (codeword), '->', decoded)

noiseless_test()
noisy_test()