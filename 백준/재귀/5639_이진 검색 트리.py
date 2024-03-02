import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def postorder_traversal(start, end):
    if start > end:
        return
    
    mid = end + 1
    for i in range(start + 1, end + 1):
        if nodes[i] > nodes[start]:
            mid = i
            break

    postorder_traversal(start + 1, mid - 1)
    postorder_traversal(mid, end)
    print(nodes[start])


nodes = []
while True:
    try:
        nodes.append(int(input()))
    except:
        break

postorder_traversal(0, len(nodes) - 1)


"""
5
45
28
24
30
60
52
98
50
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline


# def postorder_traversal(start, end):
#     if start > end:
#         return
    
#     mid = end
#     for i in range(start + 1, end):
#         if nodes[i] > nodes[start]:
#             mid = i - 1
#             print("mid:", nodes[mid])
#             break

#     postorder_traversal(start + 1, mid)
#     postorder_traversal(mid + 1, end)
#     print(nodes[start])


# nodes = []
# while True:
#     try:
#         nodes.append(int(input()))
#     except:
#         break

# postorder_traversal(0, len(nodes) - 1)