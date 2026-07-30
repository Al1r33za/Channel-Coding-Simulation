# hardware structures per clock cycle:
import gf

def bit_pop(bits :int):
	return (bits & 1), (bits >> 1)

def lfsr(taps :int, mem :int =0, /, state :int =0, sin :bool =0):

	gate1 = (state & 1)
	state |= (sin << mem)
	if(gate1):
		state ^= taps
	else:
		state  = 0
		
	state >>= 0b1

	return state

def sym2bits(k :int, B :list) -> int:
	'''map symbols to bits by k'''
	frame =0
	frames=0
	for bb in B:
		frames ^= (bb << frame)
		frame += k

	return frames

def bits2sym(k :int, S :int) -> list:
	'''map received bits to symbols by k'''
	frame =(1 << k) - 1
	Sym = []
	while S > 0:
		Sym.append(S & frame)
		S >>= k

	return Sym

def fir(taps :int, mem :int , /, state =0, sin =0):
	pass

def errpat_detect():
	pass

assert sym2bits(4, [0b0011, 0b1011, 0b0000, 0b1111]) == 0b1111_0000_1011_0011 , print(sym2bits(4, [0b0011, 0b1011, 0b0000, 0b1111]))
assert bits2sym(4, 0b1111_0000_0101_1100) == [0b1100, 0b0101, 0b0000, 0b1111] , print(bits2sym(4, 0b1111_0000_0101_1100))