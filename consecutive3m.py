num=int(raw_input())
arr=list(map(int,raw_input().split()))
s=0
for i in range(0,num-1):
    s=s+arr[i]+arr[i+1]
print(s)
