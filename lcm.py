p1,p2=map(int,raw_input().split())
maximum=1
for x in range(1,min(p1,p2)+1): 
    if p1%x==0 and p2%x==0:
        if x>maximum:
    	 maximum=x
print(maximum)
