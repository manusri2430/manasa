k=list(raw_input())
lis=[]
for i in k:
  if i in lis:
    print("yes")
    break
  else:
    lis.append(i)
else:
  print("no")
