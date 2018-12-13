n = int(raw_input())
l = sorted(list(map(int,raw_input().split())))

for i in l:
    if i < n:
        print(i),
