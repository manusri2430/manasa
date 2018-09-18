import math
a,b=map(int,raw_input().split())
c=a * b
if math.sqrt(c).is_integer():
    print "yes"
else:
    print "no"
