n = int(input())

def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return factorial(n - 1) * n

num = factorial(n)
ans = 0
for i in str(num)[::-1]:
    if i == "0":
        ans += 1
    else:
        break
        
print(ans)