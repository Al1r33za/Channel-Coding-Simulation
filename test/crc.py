# crc encode decode test module
import crc

C = (7, 4)
for u in range(16):
	u_enc = crc.encode(*C, u, g =0b1101)
	r_synd = crc.syndrome(*C, r =u_enc, g =0b1101)
	assert r_synd ==0, u_enc
