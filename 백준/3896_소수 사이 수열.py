import sys


def get_primes(n):
    is_prime = [False, False, True] + [True for _ in range(n - 2)]

    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False

    return is_prime


is_prime = get_primes(1299709)

T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    if is_prime[k]:
        print(0)
    else:
        for i in range(k - 1, -1, -1):
            if is_prime[i]:
                start = i
                break
        for i in range(k + 1, 1299709 + 1):
            if is_prime[i]:
                end = i
                break
        print(end - start)