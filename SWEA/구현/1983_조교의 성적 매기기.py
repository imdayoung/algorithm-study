import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    scores = {}
    grade = {1:"A+", 2:"A0", 3:"A-", 4:"B+", 5:"B0", 6:"B-", 7:"C+", 8:"C0", 9:"C-", 10:"D0"}

    N, K = map(int, input().split())
    for i in range(1, N + 1):
        midterm, final, assignment = map(int, input().split())
        score = midterm * 0.35 + final * 0.45 + assignment * 0.2
        scores[i] = score

    grades = sorted(scores.items(), key = lambda x:x[1], reverse = True)
    for i in range(N):
        if grades[i][0] == K:
            print(f"#{tc} {grade[i // (N // 10) + 1]}")
            break