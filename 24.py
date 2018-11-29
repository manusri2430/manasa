str = raw_input("")
try:
    i = float(str)
except (ValueError, TypeError):
    print("no")
else:
    print("yes")
