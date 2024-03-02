answer = []
 
n = int(input())
for i in range(1, n + 1):
    cnt_3 = str(i).count("3")
    cnt_6 = str(i).count("6")
    cnt_9 = str(i).count("9")
     
    cnt = cnt_3 + cnt_6 + cnt_9
    if cnt == 0:
        answer.append(str(i))
    elif cnt == 1:
        answer.append("-")
    elif cnt == 2:
        answer.append("--")
    elif cnt == 3:
        answer.append("---")
         
print(*answer)