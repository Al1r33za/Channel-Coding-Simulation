# Additive white gaussian noise channel test module ( to test eb, N0, #bit errors)
import channel as ch


b ='100101010110101111010101001000101101010111010101101101000100100100101111010101110101100000010';
r =[0] * len(b);
k = 0;
m ='';

for i in b:
	sm = ch.modulation(int(i), 2);
	r[k] = ch.awgn(sm);
	k += 1;

for i in r:
	m += str(ch.demodulation(i));
print(b, m, sep='\n');

e =0;b

for i in range(len(b)):
	e += int(b[i]) ^ int(m[i]);

print(e, e/len(b));
