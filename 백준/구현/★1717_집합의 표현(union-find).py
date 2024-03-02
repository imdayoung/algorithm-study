import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 루트 노드를 찾는 함수
def find(a):
    # 자기 자신이 루트 노드이면 반환
    if a == parent[a]:
        return a
    # a의 루트 노드 찾기
    p = find(parent[a])
    # 부노 테이블 갱신
    parent[a] = p
    # a의 루트 노드 반환
    return parent[a]


# a가 속해있는 집합과 b가 속해있는 집합을 합치는 연산
def union(a, b):
    # a, b의 루트 노드 찾기
    a = find(a)
    b = find(b)

    # a와 b의 루트 노드가 같다면 동일한 집합
    if a == b:
        return
    # 값이 더 작은 쪽이 부모 노드
    if a < b:
        parent[b] = a
    else:
        parent[a] = b 


n, m = map(int, input().split())
parent = [0] * (n + 1)
# 자기 자신을 부모로 설정
for i in range(n + 1):
    parent[i] = i

for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")