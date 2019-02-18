g=int(raw_input())
l=[int(x) for x in raw_input().split()]
c=0
if(g==len(l)):
  for i in range(0,g-1):
    for j in range(i+1,g):
         if l[i]<l[j]:
           c=c+1
print(c)
