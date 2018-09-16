c=int(raw_input())
d=c+1
p=1
while d!=0:
    e=2**p
    if d==e:
        print d
        break
    p=p+1
    d=d+1

