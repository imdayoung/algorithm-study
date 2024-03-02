import sys


def find_prime(n):
    is_prime = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
    return is_prime


N = int(sys.stdin.readline())
is_prime = find_prime(1005000)

for num in range(N, 1005000):
    if is_prime[num]:
        if str(num) == str(num)[::-1]:
            print(num)
            break