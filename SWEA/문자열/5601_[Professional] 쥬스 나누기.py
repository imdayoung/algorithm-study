T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = ["1/"+str(N) for _ in range(N)]

    print(f"#{tc}", end = " ")
    print(*lst)