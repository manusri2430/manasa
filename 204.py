n = int(raw_input())
l = list(map(int,raw_input().split()))
print(sum(list(filter(lambda x:x<0,l))))
