s = raw_input().rstrip()
newWordBegins = True
result = ''
for a in s:
	if a == ' ':
		newWordBegins = True		
	elif newWordBegins:
		newWordBegins = False
		a = chr(ord(a) - 32)
	result += a
print(result)
