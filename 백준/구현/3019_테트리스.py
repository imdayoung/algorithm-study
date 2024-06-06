import sys


def getCases(num):
    if num == 1:
        answer = block_1()
    elif num == 2:
        answer = block_2()
    elif num == 3 or num == 4:
        answer = blocks_34(num)
    else:
        answer = blocks_567(num)
    
    return answer


def block_1():
    answer = 0
    for i in range(R - 4):
        for j in range(C):
            temp = []
            temp.append([graph[i][j]])
            temp.append([graph[i + 1][j]])
            temp.append([graph[i + 2][j]])
            temp.append([graph[i + 3][j]])
            temp.append([graph[i + 4][j]])
            if temp == [[0], [0], [0], [0], [1]]:
                answer += 1
                
    for i in range(R - 1):
        for j in range(C - 3):
            temp = []
            temp.append(graph[i][j:j + 4])
            temp.append(graph[i + 1][j:j + 4])
            if temp == [[0, 0, 0, 0], [1, 1, 1, 1]]:
                answer += 1
                
    return answer
            
    
def block_2():
    answer = 0
    for i in range(R - 2):
        for j in range(C - 1):
            temp = []
            temp.append(graph[i][j:j + 2])
            temp.append(graph[i + 1][j:j + 2])
            temp.append(graph[i + 2][j:j + 2])
            if temp == [[0, 0], [0, 0], [1, 1]]:
                answer += 1
    
    return answer


def blocks_34(num):
    answer = 0
    
    if num == 3:
        comp1 = [[0, 0, 0], [0, 0, 1], [1, 1, 1]]
        comp2 = [[0, 0], [0, 0], [1, 0], [1, 1]]
    else:
        comp1 = [[0, 0, 0], [1, 0, 0], [1, 1, 1]]
        comp2 = [[0, 0], [0, 0], [0, 1], [1, 1]]
    
    for i in range(R - 2):
        for j in range(C - 2):
            temp = []
            temp.append(graph[i][j:j + 3])
            temp.append(graph[i + 1][j:j + 3])
            temp.append(graph[i + 2][j:j + 3])
            if temp == comp1:
                answer += 1
    
    for i in range(R - 3):
        for j in range(C - 1):
            temp = []
            temp.append(graph[i][j:j + 2])
            temp.append(graph[i + 1][j:j + 2])
            temp.append(graph[i + 2][j:j + 2])
            temp.append(graph[i + 3][j:j + 2])
            if temp == comp2:
                answer += 1
    
    return answer

  
def blocks_567(num):
    answer = 0
    
    if num == 5:
        comp1 = [[0, 0, 0], [0, 0, 0], [1, 1, 1]]
        comp2 = [[0, 0, 0], [1, 0, 1], [1, 1, 1]]
        comp3 = [[0, 0], [0, 0], [1, 0], [1, 1]]
        comp4 = [[0, 0], [0, 0], [0, 1], [1, 1]]
    elif num == 6:
        comp1 = [[0, 0, 0], [0, 0, 0], [1, 1, 1]]
        comp2 = [[0, 0, 0], [0, 1, 1], [1, 1, 1]]
        comp3 = [[0, 0], [0, 0], [0, 0], [1, 1]]
        comp4 = [[0, 0], [1, 0], [1, 0], [1, 1]]
    else:
        comp1 = [[0, 0, 0], [0, 0, 0], [1, 1, 1]]
        comp2 = [[0, 0, 0], [1, 1, 0], [1, 1, 1]]
        comp3 = [[0, 0], [0, 0], [0, 0], [1, 1]]
        comp4 = [[0, 0], [0, 1], [0, 1], [1, 1]]
        
    for i in range(R - 2):
        for j in range(C - 2):
            temp = []
            temp.append(graph[i][j:j + 3])
            temp.append(graph[i + 1][j:j + 3])
            temp.append(graph[i + 2][j:j + 3])
            if temp == comp1 or temp == comp2:
                answer += 1
            
    for i in range(R - 3):
        for j in range(C - 1):
            temp = []
            temp.append(graph[i][j:j + 2])
            temp.append(graph[i + 1][j:j + 2])
            temp.append(graph[i + 2][j:j + 2])
            temp.append(graph[i + 3][j:j + 2])
            if temp == comp3 or temp == comp4:
                answer += 1
                
    return answer
   

C, P = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))
R = max(heights) + 4

graph = [[0 for _ in range(C)] for _ in range(R)]
for j in range(C):
    for i in range(R - 1, R - 1 - heights[j], -1):
        graph[i][j] = 1
graph.append([1 for _ in range(C)])
R += 1

answer = getCases(P)
print(answer)