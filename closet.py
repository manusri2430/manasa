N=int(raw_input())
n1=list(map(int,raw_input().split()))
m=max(n1)
a,b=0,0
for i in range(0,len(n1)-1):
  for j in range(i+1,len(n1)):
    if abs(n1[i]+n1[j])<m:
      a,b=n1[i],n1[j]
      m=abs(a+b)
print(a,b)
