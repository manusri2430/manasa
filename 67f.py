c=int(raw_input())
fact=1
if(c==0):
    print(1)
else:
    for i in range(1,c+1):
        fact=fact*i
    print(fact)
