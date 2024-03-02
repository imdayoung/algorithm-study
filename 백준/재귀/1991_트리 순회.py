import sys
input = sys.stdin.readline

def preorder_traversal(parent):
    if parent == -19:
        return
    print(chr(parent + 65), end = "")
    preorder_traversal(tree[parent][0])
    preorder_traversal(tree[parent][1])


def inorder_traversal(parent):
    if parent == -19:
        return
    inorder_traversal(tree[parent][0])
    print(chr(parent + 65), end = "")
    inorder_traversal(tree[parent][1])


def postorder_traversal(parent):
    if parent == -19:
        return
    postorder_traversal(tree[parent][0])
    postorder_traversal(tree[parent][1])
    print(chr(parent + 65), end = "")

N = int(input())
tree = [[] for _ in range(N)]
for i in range(N):
    parent, left, right = map(str, input().split())
    parent = ord(parent) - 65
    left = ord(left) - 65
    right = ord(right) - 65
    tree[parent].append(left)
    tree[parent].append(right)

preorder_traversal(0)
print()
inorder_traversal(0)
print()
postorder_traversal(0)