def dfs(cnt, cur, start):
    if cnt == N:
        available.add(cur)
        return
    
    for i in range(start, 4):
        num = nums[i]
        dfs(cnt + 1, cur + num, i)


N = int(input())
nums = [1, 5, 10, 50]
available = set()
dfs(0, 0, 0)

print(len(available))
