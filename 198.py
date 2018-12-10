a = int(input())
l = list(map(int,raw_input().split()))
min = 10000000
max = 0
mini = -1
maxi = -1
for i in range(a):
    if l[i]>max:
        max=l[i]
        maxi=i
    if l[i]<min:
        min=l[i]
        mini=i
print(maxi-mini)
