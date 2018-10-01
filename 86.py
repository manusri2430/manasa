def isIsogram(s):
	charMap = {}
	for c in s:
		if c in charMap:
			return False
		else:
			charMap[c] = 1
	return True
e = raw_input().rstrip()
print("Yes" if isIsogram(e) else "No")
