b=int(raw_input())
rev=''
while b>0:
    rev+=str(b%10)
    b=b/10
print(rev)
