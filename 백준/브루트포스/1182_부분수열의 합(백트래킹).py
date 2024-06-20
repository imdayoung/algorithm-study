import sys
input = sys.stdin.readline

def back_tracking(idx, res):
    global cnt

    # 현재 N개의 수를 모두 넣어봤으면 종료
    if idx >= N:
        return
    
    # 합에 현재 수를 더함
    res += nums[idx]

    # 현재 합이 S라면 카운트
    if res == S:
        cnt += 1

    # 현재 idx 수를 더한 경우 탐색
    back_tracking(idx + 1, res)
    # 현재 idx 수를 더하지 않은 경우 탐색
    back_tracking(idx + 1, res - nums[idx])


N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

back_tracking(0, 0)
print(cnt)