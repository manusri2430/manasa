n,m=map(int,raw_input().split())
list=[int(x) for x in raw_input().split()]
if m in list:
    count=list.count(m)
    print count
else:
    print 0
