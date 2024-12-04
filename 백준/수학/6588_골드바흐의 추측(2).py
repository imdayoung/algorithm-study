import sys


def get_prime_numbers(n):
    is_prime = [False, False] + [True for _ in range(n - 1)]
    for i in range(3, int(n ** 0.5) + 1, 2):
        if is_prime[i]:
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
            
    return is_prime
    

n = 1000000
is_prime = get_prime_numbers(n - 1)

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    
    for i in range(3, n // 2 + 1, 2):
        if is_prime[i] and is_prime[n - i]:
            print(f"{n} = {i} + {n - i}")
            break
    else:
        print("GoldBach's conjecture is wrong.")
