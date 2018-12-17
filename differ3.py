g,h,c=raw_input().split()
c=int(c)
co=0
s=0
for i in range(len(g)):
    for j in range(len(h)):
        if(i==j):
            if(g[i]!=h[j]):
                co=co+1
            else:
                s=s+1
if(c==co):
    print('yes')
else:
    print('no')
