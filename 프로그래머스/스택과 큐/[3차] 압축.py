from collections import deque


def solution(msg):
    answer = []

    word_dict = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10,
              "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19,
              "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}
    idx = 27
    
    queue = deque(msg)
    while queue:
        temp = queue.popleft()
        while queue and temp in word_dict:
            temp += queue.popleft()
        
        if temp not in word_dict:
            word_dict[temp] = idx
            idx += 1
            queue.appendleft(temp[-1])
            temp = temp[:-1]
        
        answer.append(word_dict[temp])
    
    return answer