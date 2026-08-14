# transmitting signal using bpsk modulation through AWGN channel
import random as rn

def modulation(b :int, E =1):
	sm = (E**.5) *(1- 2*b)
	return sm

def demodulation(r):
	return 0 if r>0 else 1

def awgn(sm, N0=1):
	n = rn.normalvariate(0, (N0/2)**.5)
	r = sm + n
	return r

def AWGN(EbN0, stream, N0 =1, R =1):
	Eb =1.0
	Ec =R*Eb
	N0 = Ec / EbN0
	s = modulation(stream, Ec)
	r = awgn(s, N0)
	return demodulation(r)
