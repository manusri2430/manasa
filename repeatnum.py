h=int(raw_input())
A=(raw_input().split())
B=(raw_input()).split()
a=[]
for i in range(0,h):
    if (B[i]in A):
        a.append(B[i])
print(" ".join(a)) 
