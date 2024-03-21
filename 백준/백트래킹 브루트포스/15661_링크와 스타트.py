import sys


def make_team_start(start, start_ability):
    global answer
    link_ability = team_link_ability()
    answer = min(answer, abs(start_ability - link_ability))

    if len(team_start) == N:
        return
    
    for i in range(start, N):
        team_start.append(i)
        temp = start_ability
        for j in team_start:
            temp += S[i][j] + S[j][i]
        make_team_start(i + 1, temp)
        team_start.pop()
        

def team_link_ability():
    ability = 0
    team_link = []
    for i in range(N):
        if i not in team_start:
            team_link.append(i)

    for i in range(len(team_link)):
        for j in range(i + 1, len(team_link)):
            ability += S[team_link[i]][team_link[j]] + S[team_link[j]][team_link[i]]
    return ability


answer = int(1e9)
N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
team_start = [0]
make_team_start(1, 0)
print(answer)