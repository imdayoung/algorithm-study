def get_primes(num):
    is_prime = [False, False, True] + [True for _ in range(num - 2)]
    for i in range(2, int(num ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * 2, num + 1, i):
                is_prime[j] = False

    return is_prime


num = 10 ** 6
is_prime = get_primes(num)
print(is_prime)
for i in range(num + 1):
    if is_prime[i]:
        print(i, end = ' ')