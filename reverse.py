c=int(raw_input())
rev=''
while c>0:
    rev+=str(c%10)
    c=c/10
print(rev)
