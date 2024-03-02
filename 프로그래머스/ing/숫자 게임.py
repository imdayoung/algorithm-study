

# # 시간 초과, 런타임 에러
# answer = 0
# arr = []


# def back_tracking(a, b):
#     global answer
#     if len(arr) == len(a):
#         temp = 0
#         for i in range(len(a)):
#             if a[i] < b[arr[i]]:
#                 temp += 1
#         answer = max(answer, temp)
#         return
    
#     for i in range(len(b)):
#         if i not in arr:
#             arr.append(i)
#             back_tracking(a, b)
#             arr.pop()

            
# def solution(A, B):
#     back_tracking(A, B)
#     return answer