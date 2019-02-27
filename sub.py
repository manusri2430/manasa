import sys, string, math
N,M = map(int,raw_input().split())
L1 = list(map(int,raw_input().split()))
L2 = list(map(int,raw_input().split()))
flag = 1
for i in range(0,len(L2)) :
    if L2[i] not in L1 :
        flag = 0
        break
if flag : print('YES')
else :    print('NO')

