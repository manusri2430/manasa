def gcd(a, b):
	if a == 0:
		return b
	return gcd(b%a, a)

g, h = [int(g) for g in raw_input().split(" ")]
if g < h:
	g, h = h, g
print(gcd(g, h))
