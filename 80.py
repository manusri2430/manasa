c = int(raw_input())
digits = []
while c > 0:
	r = c % 10
	if r & 1 != 0:
		digits.append(str(r))
	c = c / 10
digits = reversed(digits) 
print(" ".join(digits))
