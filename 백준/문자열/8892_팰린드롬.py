import sys


answers = []
T = int(sys.stdin.readline())
for _ in range(T):
    flag = 0
    k = int(sys.stdin.readline())
    words = [sys.stdin.readline().rstrip() for _ in range(k)]
    for i in range(k - 1):
        for j in range(i + 1, k):
            temp = words[i] + words[j]
            temp2 = words[j] + words[i]
            if temp == temp[::-1]:
                answers.append(temp)
                flag = 1
                break
            if temp2 == temp2[::-1]:
                answers.append(temp2)
                flag = 1
                break
        if flag == 1:
            break
        
    else:
        answers.append(0)
             
for answer in answers:
    print(answer)
