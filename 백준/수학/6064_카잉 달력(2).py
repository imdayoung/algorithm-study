import sys


T = int(sys.stdin.readline())
for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    
    temp = x
    while temp <= M * N:
        if (temp - x) % M == 0 and (temp - y) % N == 0:
            print(temp)
            break
        temp += M
        
    if temp > M * N:
        print(-1)


# # 시간초과
# import sys


# T = int(sys.stdin.readline())
# for _ in range(T):
#     answer = 1
    
#     M, N, x, y = map(int, sys.stdin.readline().split())
    
#     temp_x, temp_y = 1, 1
#     while True:
#         if temp_x == x and temp_y == y:
#             print(answer)
#             break
        
#         if temp_x == M and temp_y == N:
#             print(-1)
#             break
        
#         temp_x = temp_x + 1 if temp_x < M else 1
#         temp_y = temp_y + 1 if temp_y < N else 1
            
#         answer += 1
