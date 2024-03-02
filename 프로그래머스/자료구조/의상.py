def solution(clothes):
    answer = 1
    clothes_dic = {}
    
    for cname, ctype in clothes:
        if ctype not in clothes_dic:
            clothes_dic[ctype] = 1
        else:
            clothes_dic[ctype] += 1
            
    for i in clothes_dic.values():
        answer *= (i + 1)
        
    return answer - 1