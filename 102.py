def do_stuff(input):
	a = int(input)
	
	while a & 1 == 0:
		a = a >> 1
	print(a)
		

while True:
  try:
    value = raw_input()
    do_stuff(value.rstrip()) # next line was found 
  except (EOFError):
    break #end of file reached
