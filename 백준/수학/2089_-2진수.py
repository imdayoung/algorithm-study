answer = ""

N = int(input())

if N == 0:
    answer = "0"

while N != 0 and N != 1:
    if N < 0 and N % 2 == 1:
        a = int(N / (-2)) + 1
    else:
        a = int(N / (-2))
        
    b = N + 2 * a
    N = a

    answer += str(b)

if N == 1:
    answer += "1"

print(answer[::-1])
