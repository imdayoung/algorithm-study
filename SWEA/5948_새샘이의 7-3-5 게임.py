def backtracking(start, temp):
    global sums
    
    if len(temp) == 3:
        sums.add(sum(temp))
        return
    
    for i in range(start + 1, 7):
        backtracking(i, temp + [nums[i]])


T = int(input())
for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    sums = set()
    backtracking(-1, [])
    sums = sorted(list(sums), reverse = True)
    print(f'#{test_case} {sums[4]}')