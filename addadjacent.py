n=int(raw_input())
l=list(map(int,raw_input().split()))
s=0
for i in range(0,len(l)-1):
    s=s+max(l[i],l[i+1])
print(s)
