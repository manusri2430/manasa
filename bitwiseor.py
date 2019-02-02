g = int(raw_input())
a = list(map(int,raw_input().split()))
x = a[0]
for i in range(1,g):
    x = x|a[i]
print(x)
