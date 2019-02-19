k=int(raw_input())
a=list(map(int,(raw_input()).split()))
c=[]
if (k==1):
    print(a[0])
else:
    for i in range(0,k) :
        c.append(sum(a[:i+1])+sum(a[i:]))
print(" ".join([str(i) for i in c]))
