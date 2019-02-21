k=int(raw_input())
li=list(map(int,raw_input().split()))
s=0
if k<3:
  print(k)
else:
  for i in range(k+1):
    s+=i
  print(s)
