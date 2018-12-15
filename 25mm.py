n = int(raw_input())
l = list(raw_input().split())
print(" ".join(sorted(l,key=len)))
