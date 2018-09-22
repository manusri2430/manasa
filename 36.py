import sys
paragraph = sys.stdin.read().rstrip()
specialCharCount = 0
for a in paragraph:
	if not (a.isdigit() or a.isalpha() or a.isspace()):
		specialCharCount += 1
print(specialCharCount)
