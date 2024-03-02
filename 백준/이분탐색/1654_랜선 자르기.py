'''
1654에서 마지막에 답으로 end를 출력하는 이유:
while문을 탈출하는 순간은 start == mid == end일 때임
따라서 마지막 탐색 즉 start == mid == end 일 때 마지막 if temp <= N 이 부분을 확인하는데,
만약 이 때 조건을 만족하지 않으면 현재 mid보다 1 작은 게 답이 됨,
mid == end였으므로 else end - 1을 실행하여 end - 1를 출력하면 됨,
조건을 만족하면 mid가 만족하는건데 mid == end이므로 end를 출력하게 됨
따라서 어떤 경우에서든 마지막에 end를 출력하면 됨 !!
'''

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]

start = 1
end = max(lans)

while start <= end:
    mid = (start + end) // 2
    temp = 0
    
    for lan in lans:
        temp += lan // mid

    print(start, mid, end, temp)
    if temp <= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)