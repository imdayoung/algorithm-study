import sys
import copy


def get_block_element(num):
    temp = [[1 for _ in range(3)] for _ in range(2)]
    block3 = copy.deepcopy(temp)
    block4 = copy.deepcopy(temp)
    block5 = copy.deepcopy(temp)
    block6 = copy.deepcopy(temp)
    block7 = copy.deepcopy(temp)
    
    block3[0][0], block3[1][2] = 0, 0
    block4[0][2], block4[1][0] = 0, 0
    block5[0][0], block5[0][2] = 0, 0
    block6[0][0], block6[0][1] = 0, 0
    block7[0][1], block7[0][2] = 0, 0

    blocks = [
        [[1 for _ in range(1)] for _ in range(4)],
        [[1 for _ in range(2)] for _ in range(2)],
        block3, block4, block5, block6, block7
    ]
    
    return blocks[num - 1]


# 놓을 수 있는 곳인지 확인
# def is_puttable(x, y, block):
#     for i in range(x, x + block_height):
#         for j in range(y, y + block_width):
#             if 
            
    

answer = 0

C, P = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))
R = max(heights) + 4

graph = [[0 for _ in range(C)] for _ in range(R)]
for j in range(C):
    for i in range(R - 1, R - 1 - heights[j], -1):
        graph[i][j] = 1
# for g in graph:
#     print(g)
    
block = get_block_element(P)
block_height = len(block)
block_width = len(block[0])
# for b in block:
#     print(b)

# for i in range(R - 1):
#     for j in range(C - 1):
#         if is_puttable(i, j, block):
#             answer += 1

print(answer)