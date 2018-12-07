L,R=map(int,raw_input().split())
if(L>R):
    min2=L
else:
    min2=R
while(1):
    if(min2%L==0 and min2%R==0):
        print(min2)
        break
    min2=min2+1

