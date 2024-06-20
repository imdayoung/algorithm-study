D, K = map(int, input().split())

A_fibo = [0] * D
B_fibo = [0] * D
A_fibo[0], A_fibo[1] = 1, 0
B_fibo[0], B_fibo[1] = 0, 1

for i in range(2, D):
    A_fibo[i] = A_fibo[i - 1] + A_fibo[i - 2]
    B_fibo[i] = B_fibo[i - 1] + B_fibo[i - 2]

# A_fibo[D - 1] * A + B_fibo[D - 1] * B = K 를 만족하는 A, B 구하기
a = A_fibo[D - 1]
b = B_fibo[D - 1]
for i in range(1, K // A_fibo[D - 1] + 1):
    if (K - a * i) % b == 0:
        print(i)
        print((K - a * i) // b)
        break