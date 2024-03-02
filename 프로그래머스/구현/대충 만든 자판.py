def solution(keymap, targets):
    answer = []
    
    for target in targets:
        ans = 0
        
        for word in target:
            cnt = 10001
            for key in keymap:
                if cnt > key.find(word) + 1 and key.find(word) != -1:
                    cnt = key.find(word) + 1
            ans += cnt
        answer.append(-1) if ans >= 10001 else answer.append(ans)
        
    return answer