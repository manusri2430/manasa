h=int(raw_input())
a=[]
for x in range(1,h+1):
    if(h%x==0 and h%2!=0):
        a.append(x)
s=" ".join(map(str,a))
print(s)
