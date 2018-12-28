def rat(k,n):
    print(k[n:]+k[:n])
k,n=map(str,raw_input().split())
n=int(n)
m=len(k)-n
rat(k,m)
