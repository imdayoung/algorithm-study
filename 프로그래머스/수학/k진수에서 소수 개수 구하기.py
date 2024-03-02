def solution(n, k):
    answer = 0
    
    # k진수로 변환
    num = ""
    while n > 0:
        n, mod = divmod(n, k)
        num += str(mod)
    num = num[::-1]
    
    # 0으로 스플릿
    nums = []
    temp = num.split("0")
    for t in temp:
        if t != "":
            t = int(t)
            nums.append(t)
    
    # 소수인지 판별
    for n in nums:
        print(n)
        if n == 1:
            continue
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                break
        else:
            answer += 1
            
    return answer

# # 런타임 에러
# def get_prime(n):
#     is_prime = [False, False] + [True] * (n - 1)
#     for i in range(2, int(n ** 0.5) + 1):
#         if is_prime[i]:
#             for j in range(i * 2, n + 1, i):
#                 is_prime[j] = False
#     return is_prime


# def solution(n, k):
#     answer = 0
    
#     # k진수로 변환
#     num = ""
#     while n > 0:
#         n, mod = divmod(n, k)
#         num += str(mod)
#     num = num[::-1]
    
#     # 0으로 스플릿
#     nums = []
#     max_val = 0
#     temp = num.split("0")
#     for t in temp:
#         if t != "":
#             t = int(t)
#             max_val = max(max_val, t)
#             nums.append(t)
    
#     # 소수인지 판별
#     is_prime = get_prime(max_val)
#     for n in nums:
#         if is_prime[n]:
#             answer += 1
            
#     return answer