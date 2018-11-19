A,B,C=[int(x) for x in raw_input().split()]
sum=0
for i in range(C):
    sum+=A+(i*B)
print(sum)
