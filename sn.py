def isomorphic(p1,p2):
    diff = [-26]*26
    if len(p1)!=len(p2):
        return "no"
    for i in range(len(p1)):
        a = ord(p1[i])
        b = ord(p2[i])
        position = a-97
        new_diff = a-b
        if diff[position]==-26:
            diff[position]=new_diff
        elif diff[position]!=new_diff:
            return "no"
    return "yes"

p1,p2 = raw_input().split()
print(isomorphic(p1,p2))
