f=int(raw_input())
rev=''
while f>0:
    rev+=str(f%10)
    f=f/10
print(rev)
