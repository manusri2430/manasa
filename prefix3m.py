num=int(raw_input())
arr=list(map(int,raw_input().split()))
m=[arr[0]]
for i in range(2,num+1) :
    m.append(sum(arr[:i]))
print(" ".join([str(i) for i in m]))
