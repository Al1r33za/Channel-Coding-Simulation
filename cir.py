# hardware structures per clock cycle:

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

def fir(taps :int, mem :int , /, state =0, sin =0):
	pass
def errpat_detect():
	pass

