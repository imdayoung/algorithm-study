import sys
input = sys.stdin.readline


def back_tracking(x):
    global answer
    # 확인 종료 및 리턴
    if len(energy) == 2:
        answer = max(answer, x)
        return
    
    for i in range(1, len(energy) - 1):
        collect = energy[i - 1] * energy[i + 1]
        x += collect
        temp = energy[i]
        del energy[i]
        back_tracking(x)
        # 복구
        x -= collect
        energy.insert(i, temp)
    

N = int(input())
energy = list(map(int, input().split()))
answer = 0
back_tracking(0)
print(answer)