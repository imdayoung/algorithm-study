T = int(input())
dic = {}
for i in range(1, 300):
    dic[i * (i + 1) // 2] = i

dic2 = {v:k for k, v in dic.items()}

for tc in range(1, T + 1):
    p, q = map(int, input().split())
    x, y = 0, 0
    for i in range(1, 300):
        temp = i * (i + 1) // 2
        if temp >= p:
            interval = temp - p
            x += (dic[temp] - interval)
            y += (1 + interval)
            break

    for i in range(1, 300):
        temp = i * (i + 1) // 2
        if temp >= q:
            interval = temp - q
            x += (dic[temp] - interval)
            y += (1 + interval)
            break
    
    interval = y - 1
    x += interval
    print(f'#{tc} {dic2[x] - interval}')