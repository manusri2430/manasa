a=int(raw_input())
rev=''
while a>0:
    rev+=str(a%10)
    a=a/10
print(rev)
