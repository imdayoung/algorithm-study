import sys
input = sys.stdin.readline

max = 1000000
is_prime = [False, False] + [True] * (max - 1)
for i in range(3, int(max ** 0.5) + 1, 2):
    if is_prime[i]:
        for j in range(i * 2, max + 1, i):
            is_prime[j] = False

while True:
    n = int(input().rstrip())
    if n == 0:
        break

    for i in range(3, n // 2 + 1, 2):
        if is_prime[i] and is_prime[n - i]:
            print(n,"=",i,"+",n - i)
            break
    else:
        print("Goldbach's conjecture is wrong.")