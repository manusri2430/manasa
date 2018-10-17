c = int(raw_input())
product = 1
while c > 0:
	product *= c%10
	c = c / 10
print(product)
