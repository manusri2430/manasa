n,x = map(int,raw_input().split())
l = list(map(int,raw_input().split()))
flag = False
for i in l:
    for j in l:
        if i+j == x:
            flag=True
            break
    if flag:
        break
if flag:
    print('yes')
else:
    print('no')
