g = raw_input().rstrip()
digits = []
for c in g:
	if c.isdigit():
		digits.append(c)
print("".join(digits))
