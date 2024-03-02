T = int(input())
for tc in range(1, T + 1):
    print(f"#{tc}")
    N = int(input())
     
    doc = ""
    length = 0
    for _ in range(N):
        Ci, Ki = input().split()
        doc += Ci * int(Ki)
        length += int(Ki)
         
    i = 0
    for _ in range(length // 10):
        print(doc[i : i + 10])
        i += 10
    print(doc[i:])