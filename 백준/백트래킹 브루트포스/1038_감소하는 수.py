def back_tracking(num, digit):
    if num != "":
        decreasing_nums.append(int(num))

    for i in range(digit - 1, -1, -1):
        back_tracking(num + str(i), i)


decreasing_nums = []
back_tracking("", 10)
decreasing_nums.sort()

N = int(input())
if N > len(decreasing_nums) - 1:
    print(-1)
else:
    print(decreasing_nums[N])


# # 시간초과
# N = int(input())
# answer = -1
# idx = -1

# for num in range(0, 9876543210 + 1):
#     temp = [n for n in str(num)]
#     if temp == sorted(list(set(temp)), reverse = True):
#         idx += 1
#     if idx == N:
#         answer = int(''.join(n for n in temp))
#         break

# print(answer)