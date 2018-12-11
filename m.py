c,d=map(int,raw_input().split())
count=0
for i in range(c,d+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            count=count+1
print count
