n=int(raw_input())
a=(raw_input()).split()
b=[]
for i in range(0,n):
    for j in range(i+1,n):
        b.append(max(a[i],a[j]))
    break
print(" ".join(b))
