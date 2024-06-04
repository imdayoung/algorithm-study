import sys


def block_1():
    answer = 0
    # 세로
    for i in range(R - 2):
        for j in range(C):
            temp = []
            temp.append([graph[i][j]])
            temp.append([graph[i + 1][j]])
            temp.append([graph[i + 2][j]])
            temp.append([graph[i + 3][j]])
            if temp == [[0], [0], [0], [1]]:
                answer += 1
    # 가로 엥
    # for i in range(R):
    #     for j in range(C - 4):
    #         temp = []
    #         temp.append(graph[i][j:j+4])
    #         if temp == []:
    #             answer += 1
    return answer
            
    
def block_2():
    answer = 0
    
    
def block_3():
    answer = 0
    
    
def block_4():
    answer = 0
    
    
def block_5():
    answer = 0
    
    
def block_6():
    answer = 0
    
    
def block_7():
    answer = 0
   

def getCases(num):
    answer = 0
    
    if num == 1:
        answer = block_1()
    elif num == 2:
        answer = block_2()
    elif num == 3:
        answer = block_3()
    elif num == 4:
        answer = block_4()
    elif num == 5:
        answer = block_5()
    elif num == 6:
        answer = block_6()
    else:
        answer = block_7()
        
    return answer
    

C, P = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))
R = max(heights) + 4

graph = [[0 for _ in range(C)] for _ in range(R)]
for j in range(C):
    for i in range(R - 1, R - 1 - heights[j], -1):
        graph[i][j] = 1
graph.append([1 for _ in range(C)])
# for g in graph:
#     print(g)

answer = getCases(P)
print(answer)