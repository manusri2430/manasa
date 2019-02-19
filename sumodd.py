g,k=map(int,raw_input().split())
s=0
for i in range(g,k+1):
  if i%2!=0:
    s+=i
print(s)
