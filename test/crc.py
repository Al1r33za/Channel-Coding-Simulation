# crc encode decode test module
import crc

assert crc.encode(0b0000, 0b1101, 4) == int(0b0000000)
assert crc.encode(0b1111, 0b1101, 4) == int(0b1111111)
assert crc.encode(0b0011, 0b1101, 4) == int(0b0100011), bin(crc.encode(0b0011, 0b1101))
assert crc.encode(0b1110, 0b1101, 4) == int(0b0101110)
assert crc.encode(0b1011, 0b1101, 4) == int(0b1001011)

''' k (length of massage) must be included. 0b0011 -> bit_length() -> 2 ~= 4
for Block Codes stream Code must be framed into k bits '''

for u in range(16):

	u_enc = crc.encode(u, 0b1101, 4)
	assert crc.syndrome_chk(u_enc, 0b1101, 7, 4) == 0
