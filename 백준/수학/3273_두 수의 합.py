# import sys
# input = sys.stdin.readline

# ans = 0
# n = int(input().rstrip())
# lst = list(map(int, input().rstrip().split()))
# x = int(input().rstrip())
# lst.sort()

# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if lst[i] + lst[j] == x:
#             ans += 1
#             break
#         if lst[i] + lst[j] > x:
#             break
#     if lst[i] > x // 2:
#         break
            
# print(ans)

count = 0

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
i, j = 0, n - 1

while i < j:
    temp = arr[i] + arr[j]
    if temp == x:
        count += 1
        i += 1
        j -= 1
    elif temp < x:
        i += 1
    else:
        j -= 1
print(count)