from collections import deque


def is_transable(begin, target, n):
    diff = 0
    for i in range(n):
        if begin[i] != target[i]:
            diff += 1

    if diff == 1:
        return True
    return False


def solution(begin, target, words):
    if target not in words:
        return 0
    
    n = len(words[0])
    m = len(words)
    queue = deque()
    visited = [0] * m

    for i in range(m):
        if is_transable(begin, words[i], n):
            queue.append(i)
            visited[i] = 1

    while queue:
        cur_word_idx = queue.popleft()
        if words[cur_word_idx] == target:
            return visited[cur_word_idx]
        for i in range(m):
            next_word = words[i]
            if not visited[i] and is_transable(words[cur_word_idx], next_word, n):
                queue.append(i)
                visited[i] = visited[cur_word_idx] + 1

    return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
# 4

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
# 0