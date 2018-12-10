a = int(raw_input())
l1 = list(map(int,raw_input().split()))
l2 = list(map(int,raw_input().split()))
if set(l1)==set(l2):
    print("yes")
else:
    print("no")
