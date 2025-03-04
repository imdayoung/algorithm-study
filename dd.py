def dfs(cur, n, idx, candidates):
    
    if len(cur) == n:
        # print("candidate: ", cur)
        cur.sort()
        temp = ''.join(str(a) for a in cur)
        result.add(temp)
        
    if len(cur) == n or idx > n - 1:
        return
    
    for i in range(len(candidates[idx])):
        if candidates[idx][i] not in cur:
            dfs(cur + [candidates[idx][i]], n, idx + 1, candidates)


def is_candidate(u_id, b_id):
    if len(u_id) != len(b_id):
        return False
    
    for i in range(len(b_id)):
        if u_id[i] != b_id[i] and b_id[i] != '*':
            return False
        
    return True


def solution(user_id, banned_id):
    answer = 0
    
    n, m = len(banned_id), len(user_id)
    candidates = [[] for _ in range(n)]
    
    for i in range(n):
        b_id = banned_id[i]
        
        for j in range(m):
            u_id = user_id[j]
            if is_candidate(u_id, b_id):
                candidates[i].append(j)
    
    print(candidates)
    dfs([], n, 0, candidates)
    print("result:",result)
    
    return answer

result = set()
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
result = set()
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
result = set()
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
result = set()
solution(["abcd", "bedf", "evaf", "egas", "ryas", "weta", "aget", "shrt"], ["****", "****", "****", "****", "****", "****", "****", "****"])