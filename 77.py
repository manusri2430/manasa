a=int(raw_input())
count=0
if a>0:
    for i in range(1,a+1):
        if a%i==0:
            print i,
