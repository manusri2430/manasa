h=int(raw_input())
b=[]
while(h>0):
    dig=h%10
    b.append(dig)
    h=h//10
print sum(b)
