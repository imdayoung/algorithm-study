# N개의 강의를 M개로 분할
# M개의 블루레이에 녹화된 동영상의 길이의 최댓값이 최소가 되도록
N, M = map(int, input().split())
lengths = list(map(int, input().split()))

start = max(lengths)
end = sum(lengths)
answer = end

while start <= end:
    mid = (start + end) // 2
    div = 0
    temp = 0

    for i in range(len(lengths)):
        if temp + lengths[i] <= mid:
            temp += lengths[i]
        else:
            div += 1
            temp = 0
            temp += lengths[i]
    div += 1

    if div <= M:
        end = mid - 1
        answer = mid
    elif div > M:
        start = mid + 1

print(answer)


'''
# N개의 강의를 M개로 분할
# M개의 블루레이에 녹화된 동영상의 길이의 최댓값이 최소가 되도록
# 역시나 시간 초과 쩝
N, M = map(int, input().split())
lengths = list(map(int, input().split()))

mid1, mid2 = 1, N - 2
res = sum(lengths[-2:])

for i in range(mid2 - mid1):
    len1 = sum(lengths[:mid1 + i])
    for j in range(mid2 - i):
        len2 = sum(lengths[mid1 + i:mid2 - j])
        len3 = sum(lengths[mid2 - j:])
        temp = len1 + len2 + len3
        if temp < res:
            res = temp   

print(res)
'''