g= int(raw_input())
reversed = ''
while g > 0:
	reversed += str(g%10)
	g = g / 10
print(reversed)
