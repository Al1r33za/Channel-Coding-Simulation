from lrsolve import chien_search
from gf import exfield_gen, mul

f16 = exfield_gen(4, 0b11001)
a =f16[0]

def chien_test():
    L =[a[0], a[7]]
    print(chien_search(L, f16))
    L =[a[4], a[9], a[0]]
    print(chien_search(L, f16))

chien_test()