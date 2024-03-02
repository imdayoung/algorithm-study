import sys
input = sys.stdin.readline

N = int(input())
R = int(input())
recommends = list(map(int, input().split()))

frames = {}
for student in recommends:
    # 추천 학생이 사진틀에 있는 경우
    if student in frames:
        frames[student] += 1

    # 사진틀이 꽉 차지 않았고 추천 학생이 사진틀에 없는 경우
    elif len(frames) < N:
        frames[student] = 1

    # 사진틀이 꽉 찼는데 추천 학생이 사진틀에 없는 경우 지우고 추가
    else:
        min_value = min(frames.values())
        for std, cnt in frames.items():
            if cnt == min_value:
                del frames[std]
                break
        frames[student] = 1

answer = sorted(list(frames.keys()))
print(*answer)