n=int(raw_input())
m=n+1
i=1
while m!=0:
    k=2**i
    if m==k:
        print m
        break
    i=i+1
    m=m+1
