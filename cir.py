# hardware structures per clock cycle:
import gf

def bit_pop(bits :int):
	return (bits & 1), (bits >> 1)

def lfsr(taps :int, mem :int, /, state :int =0, sin :bool =0):
	'''lfsr hardware model(per clock cycle).

	Key Arguments:
	taps -- feedback taps of lfsr
	mem -- order of lfsr or number of regs
	state -- state of each regs in each cycle
	sin -- input serial (bit streams)
	'''
	gate1 = (state & 1)
	state |= (sin << mem)
	if(gate1):
		state ^= taps
		
	state >>= 1

	return state

def fir(taps :int, mem :int , /, state :int=0, sin :bool=0):
	'''fir hardware model(per clock cycle).

	Key Arguments:
	taps -- feedforward taps of fir
	mem -- order of fir or number of regs
	state -- state of each regs in each cycle
	sin -- input serial (bit streams)
	'''
	gate = (state & taps) % 2
	state |= ((sin << mem) >> 1)

	return gate

def sym2bits(k :int, s :int):
	'''map symbols to bits by k'''
	for i in range(k):
		yield (s >> i) & 1

def bits2sym(B :list):
	'''map received bits to symbols'''
	s = 0
	for i, bb in enumerate(B):
		s += (bb << i)

	return s


def errpat_detect():
	pass

# assert sym2bits(4, [0b0011, 0b1011, 0b0000, 0b1111]) == 0b1111_0000_1011_0011 , print(sym2bits(4, [0b0011, 0b1011, 0b0000, 0b1111]))
# assert bits2sym(4, 0b1111_0000_0101_1100) == [0b1100, 0b0101, 0b0000, 0b1111] , print(bits2sym(4, 0b1111_0000_0101_1100))