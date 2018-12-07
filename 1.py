h=int(raw_input())
fact=1
if(h==0):
    print(1)
else:
    for i in range(1,h+1):
        fact=fact*i
    print(fact)
