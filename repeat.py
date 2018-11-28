string=str(raw_input(""))
a=[0]*256
maxi=-1
for x in string:
	a[ord(x)]+=1
for x in string:
	if maxi<a[ord(x)]:
		ans=x
print(ans)
