N = int(input())

fact = 1
for i in range(2, N + 1):
    fact *= i
    
    while str(fact)[-1] == '0':
        fact //= 10
        
    fact %= 1000000000000000000
    
print(str(fact)[-5:])
