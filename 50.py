a = int(raw_input())
print("yes" if a != 0 and (a & (a-1) ==0) else "no")
