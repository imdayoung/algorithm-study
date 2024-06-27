import sys


def get_prime_numbers():
    # MAX = 100000001
    MAX = 20
    is_prime = [True for _ in range(MAX)]
    is_prime[0] = False
    is_prime[1] = False
    
    for i in range(2, int(MAX ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * 2, MAX, i):
                is_prime[j] = False
    
    return is_prime
    

a, b = map(int, sys.stdin.readline().split())
prime_numbers = get_prime_numbers()
for number in range(a, b + 1):
    if prime_numbers[number]:
        print(number)