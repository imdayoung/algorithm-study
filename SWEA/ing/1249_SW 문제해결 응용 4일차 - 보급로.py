import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    graph = []
    
    for _ in range(n):
        temp = list(map(int, input()))
        graph.append(temp)


    
    print(f'#{tc}')