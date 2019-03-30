import os
k=[]
r=int(raw_input())
for i in range(r):
    a=str(raw_input())
    k.append(a)
print(os.path.commonprefix(k))
