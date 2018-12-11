h = list(raw_input())
for i in range(0,len(h),2):
    h[i],h[i+1] = h[i+1],h[i]

print("".join(h))
