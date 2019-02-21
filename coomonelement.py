N,M=(raw_input()).split()
N,M=int(N),int(M)
a=list(map(int,(raw_input()).split()))
k=[]
h=[]
c=a[:N]
d=a[N:]
for i in c:
    if(i in d):
        h.append(i)
        d.remove(i)
h=sorted(h)        
print(" ".join([str(i) for i in h]))
