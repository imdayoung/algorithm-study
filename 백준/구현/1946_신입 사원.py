import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    answer = 1
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]
    scores = sorted(scores, key = lambda x : x[0])  # 서류 심사 성적 순위를 기준으로 정렬

    # 서류 심사 성적 순위가 1등인 지원자의 면접 성적 순위를 기준으로 설정
    # standard보다 성적이 좋아야 선발될 수 있음
    standard = scores[0][1]

    for i in range(1, N):
        # 현재 기준 면접 성적 순위보다 높으면 선발 후 해당 참여자의 면접 성적 순위를 기준으로 설정
        if scores[i][1] < standard:
            answer += 1
            standard = scores[i][1]

    print(answer)