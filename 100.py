a = int(raw_input())
product = 1
while a > 0:
	product *= a%10
	a = a / 10
print(product)
