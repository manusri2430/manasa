def gcd(a, b):
	if a == 0:
		return b
	return gcd(b%a, a)

c, d = [int(c) for c in raw_input().split(" ")]
if c < d:
	c, d = d, c
print((c * d) / gcd(c, d))
