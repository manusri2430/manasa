x1,y1=map(int,raw_input().split())
x2,y2=map(int,raw_input().split())
x3,y3=map(int,raw_input().split())
a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) 
if a==0:
    print("yes")
else:
    print("no")
