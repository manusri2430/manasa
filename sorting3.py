n,k=map(int,raw_input().split())
b=list(map(int,raw_input().split()))
m=list(map(int,raw_input().split()))
p=b+m
p.sort()
s=""
for i in range(0,len(p)):
        s=s+str(p[i])+" "
print(s.strip())
