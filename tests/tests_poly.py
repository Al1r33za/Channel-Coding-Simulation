from gf import exfield_gen
import poly as p

f16 = exfield_gen(4, 0b11001)
a =f16[0]

def conv_test():
    print(p.conv([a[0], a[0], a[5]], [a[0], a[10], a[0]], f16))

def eval_test():
    print(p.eval([a[0], a[1], a[1], a[0]], a[1], f16))
    print(p.eval([0, 0, 0, a[0]], a[1], f16))

def diff_test():
    print(p.diff([8, 2, 15]))

# conv_test()
# eval_test()
diff_test()