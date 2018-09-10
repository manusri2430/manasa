def fibonacci(a):
    if a == 1:
        return 1
    elif a == 0:
        return 0 
    else:
        return fibonacci(a-1) + fibonacci(a-2)

number = int(raw_input())
for i in range(number):
    print(fibonacci(i)),
