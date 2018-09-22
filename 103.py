s = raw_input().rstrip()
newWordBegins = True
result = ''
for b in s:
	if b == ' ':
		newWordBegins = True		
	elif newWordBegins:
		newWordBegins = False
		b = chr(ord(b) - 32)
	result += b
print(result)
