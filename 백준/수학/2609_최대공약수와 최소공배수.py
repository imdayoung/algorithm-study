x, y = map(int, input().split())
a, b = 0, 0

if x < y:
    a, b = y, x
else:
    a, b = x, y

while b > 0:
    a, b = b, a % b
    
print(a)
print(x * y // a)