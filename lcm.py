n1,n2=map(int,raw_input().split())
maximum=1
for x in range(1,min(n1,n2)+1): 
    if n1%x==0 and n2%x==0:
        if x>maximum:
    	 maximum=x
print(maximum)
