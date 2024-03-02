from collections import deque


def solution(elements):
    sums = set()
    sums.add(sum(elements))
    
    n = len(elements)
    elements = deque(elements)
    
    for _ in range(n):
        temp = [i for i in elements]
        for i in range(1, n):
            sums.add(sum(temp[:i]))
        elements.append(elements.popleft())
        
    return len(sums)