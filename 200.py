o=str(raw_input())
print(''.join([j for i,j in enumerate(o) if j not in o[:i]]))
