import math
i,r =map(int,raw_input().split())
count=0
for q in range(i,r):
  if int(math.sqrt(q))**2==q:
      count=count+1
print(count) 
