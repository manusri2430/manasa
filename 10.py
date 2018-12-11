def diffOne(p1,p2):
    diff = 2
    for i in range(len(p1)):
        if p1[i]!=p2[i] and diff:
            diff-=1
        if not diff:
            return "no"
    return "yes"

p1, p2 = list(raw_input().split())
print(diffOne(p1,p2))
