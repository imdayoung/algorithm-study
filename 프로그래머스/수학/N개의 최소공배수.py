from collections import defaultdict


def get_prime(n):
    primes = []
    is_prime = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
                
    for i in range(len(is_prime)):
        if is_prime[i]:
            primes.append(i)
    return primes


def solution(arr):
    answer = 1
    primes = get_prime(100)
    divisor = defaultdict(int)
    
    for num in arr:
        temp = num
        
        for p in primes:
            # 해당 소수가 num의 약수인 경우
            if temp % p == 0:
                cnt = 0
                while temp % p == 0:
                    cnt += 1
                    temp = temp // p
                divisor[p] = max(divisor[p], cnt)
            
    for d in divisor:
        answer *= d ** divisor[d]
        
    return answer