import sys
input = sys.stdin.readline

N = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

start, end = 0, N - 1

# 최대 최소를 구하는 문제에서 초기화 잘 하기
# 문제에서 나올 수 있는 최댓값보다 크게, 최솟값보다 작게 설정
# 투포인터 -> 움직이기 위한 조건 잘 생각 
answer = liquids[-1] + liquids[-2]
while start != end:
    temp = liquids[start] + liquids[end]
    if temp > 0:
        if answer > abs(temp):
            i, j = start, end 
            answer = abs(temp)   
        end -= 1
    
    elif temp < 0:
        if answer > abs(temp):
            i, j = start, end
            answer = abs(temp)
        start += 1

    else:
        i, j = start, end
        break    

print(liquids[i], liquids[j])