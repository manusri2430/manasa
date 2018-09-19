c,d=map(int,raw_input().split())
list=[int(x) for x in raw_input().split()]
if h in list:
    count=list.count(h)
    print count
else:
    print 0
