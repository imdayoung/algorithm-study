import sys
sys.setrecursionlimit(10 ** 7)

def solution(n):
    d = [0] * (n + 1)
    
    def fibo(n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        if d[n] != 0:
            return d[n]
        d[n] = fibo(n - 2) + fibo(n - 1)
        return d[n]
    
    return fibo(n) % 1234567