x,y,z=map(int,raw_input().split())
if((x * x) + (y * y) == (z * z)) or ((x * x) + (z * z) == (y * y)) or ((z * z) + (y * y) == (x * x)):
    print("yes")
else:
    print("no")
 
