def catalan(n): 
    if n <=1 : 
        return 1 
    res = 0 
    for i in range(n): 
        res += catalan(i) * catalan(n-i-1)   
    return res 

for i in range(int(raw_input())+1):
    print(catalan(i)),
