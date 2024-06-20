import sys
input = sys.stdin.readline

def fibo(n):
    for i in range(2, n):
        zeros.append(zeros[i - 1] + zeros[i])
        ones.append(ones[i - 1] + ones[i])
    
zeros = [1, 0, 1]
ones = [0, 1, 1]
fibo(40)

T = int(input())
for _ in range(T):
    N = int(input())
    print(zeros[N], ones[N])