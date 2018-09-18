n=int(raw_input())
count=0
if n>1:
    for i in range(2,n):
        if n%i==0:
            count=count+1
if count>1:
    print "yes"
else:
    print "no"
