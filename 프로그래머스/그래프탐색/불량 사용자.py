result = set()

def dfs(cur, n, idx, candidates):
    if len(cur) == n:
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
    n, m = len(banned_id), len(user_id)
    candidates = [[] for _ in range(n)]
    
    for i in range(n):
        b_id = banned_id[i]
        
        for j in range(m):
            u_id = user_id[j]
            if is_candidate(u_id, b_id):
                candidates[i].append(j)
    
    dfs([], n, 0, candidates)
    
    return len(result)