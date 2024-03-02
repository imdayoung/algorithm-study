T = 10
for _ in range(T):
    ladder = []
    tc = int(input())
    for _ in range(100):
        temp = list(map(int, input().split()))
        ladder.append(temp)
    X = ladder[99].index(2)
    
    for i in range(99, -1, -1):
        if X < 99 and ladder[i][X + 1] == 1:
            while X < 99 and ladder[i][X + 1] == 1:
                X += 1
                
        elif X > 0 and ladder[i][X - 1] == 1:
            while X > 0 and ladder[i][X - 1] == 1:
                X -= 1
        
    print(f'#{tc} {X}')