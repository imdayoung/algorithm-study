import sys


def matrix_multiply(matrix_a, matrix_B):
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += matrix_a[i][k] * matrix_B[k][j]

    for i in range(N):
        for j in range(N):
            result[i][j] %= 1000

    return result

def recursive(matrix, n):
    if n == 1:
        return matrix
    if n % 2 == 0:
        temp = recursive(matrix, n // 2)
        return matrix_multiply(temp, temp)
    else:
        temp = recursive(matrix, n - 1)
        return matrix_multiply(temp, matrix)


N, B = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = recursive(A, B)
    
for row in result:
    for num in row:
        print(num % 1000, end = ' ')
    print()

# 1629 곱셈 참고

# # 시간 초과
# import sys
# import copy


# def matrix_multiply(matrix_a, matrix_B):
#     result = [[0 for _ in range(N)] for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             for k in range(N):
#                 result[i][j] += matrix_a[i][k] * matrix_B[k][j]
#             result[i][j] = result[i][j] % 1000

#     return result

# N, B = map(int, sys.stdin.readline().split())
# A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# A_temp = copy.deepcopy(A)

# for _ in range(B - 1):
#     A = matrix_multiply(A, A_temp)
    
# for a in A:
#     print(*a)