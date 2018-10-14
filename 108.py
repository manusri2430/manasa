a, b, d = [int(x) for x in raw_input().split(" ")]
sum = 0
for i in range(d):
	sum += a + (i * b)
print(sum)
