b=int(raw_input())
print("yes" if b != 0 and (b & (b-1) ==0) else "no")
