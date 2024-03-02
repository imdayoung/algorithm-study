def solution(n, words):
    end = words[0][0]
    
    for i in range(len(words)):
        if words[i] in words[:i] or words[i][0] != end:
            x = n if (i + 1) % n == 0 else (i + 1) % n
            if (i + 1) % n == 0:
                y = (i + 1) // n
            else:
                y = (i + 1) // n + 1
            return [x, y]
        end = words[i][-1]
    
    return [0, 0]