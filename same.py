L,R=map(int,raw_input().split())
if(L>R):
    min1=L
else:
    min1=R
while(1):
    if(min1%L==0 and min1%R==0):
        print(min1)
        break
    min1=min1+1

