import sys
input = sys.stdin.readline

def back_tracking(start):
    global answer
    if len(team_1) == N // 2:
        team_2 = []
        for i in range(2, N + 1):
            if i not in team_1:
                team_2.append(i)

        ability_1, ability_2 = 0, 0
        for i in range(N // 2):
            for j in range(i + 1, N // 2):
                ability_1 += S[team_1[i]][team_1[j]] + S[team_1[j]][team_1[i]]
                ability_2 += S[team_2[i]][team_2[j]] + S[team_2[j]][team_2[i]]
        answer = min(answer, abs(ability_1 - ability_2))
        return
    
    for i in range(start, N + 1):
        team_1.append(i)
        back_tracking(i + 1)
        team_1.pop()


answer = int(1e9)
N = int(input())
S = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    temp = list(map(int, input().split()))
    for j in range(1, N + 1):
        S[i][j] = temp[j - 1]

team_1 = [1]
back_tracking(2)
print(answer)