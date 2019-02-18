k=int(raw_input())
n=list(map(int,raw_input().split()))
for x in range(0,k-1,2):
    n[x],n[x+1]=n[x+1],n[x]
j=" ".join(map(str,n))
print(j)
