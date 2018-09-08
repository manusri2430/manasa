num1,num2=map(int,raw_input().split())
num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2
print(num1),
print(num2)
