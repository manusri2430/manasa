n =int(raw_input())
a = list(map(int,raw_input().split()))
a.sort()
print(a[n-1]-a[0])
