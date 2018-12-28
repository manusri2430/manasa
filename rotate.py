def rat(g,h):
    print(g[h:]+g[:h])
g,h=map(str,raw_input().split())
h=int(h)
m=len(g)-h
rat(g,m)
