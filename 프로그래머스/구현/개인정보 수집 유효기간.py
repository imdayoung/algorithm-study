def solution(today, terms, privacies):
    answer = []
    privacies_dic = {}
    year_today = int(today.split(".")[0])
    month_today = int(today.split(".")[1])
    day_today = int(today.split(".")[2])
    
    for i in terms:
        privacies_dic[i.split()[0]] = int(i.split()[1])
    
    for i in range(len(privacies)):
        p = privacies[i]
        year_due = int(p.split()[0].split(".")[0])
        month_due = int(p.split()[0].split(".")[1])
        day_due = int(p.split()[0].split(".")[2]) - 1

        month_due += privacies_dic[p.split()[1]] % 12
        year_due += privacies_dic[p.split()[1]] // 12
        
        if day_due == 0:
            month_due -= 1
            day_due = 28
        
        if month_due > 12:
            year_due += 1
            month_due -= 12
        
        if month_due == 0:
            month_due = 12
        
        if year_today > year_due or (year_today == year_due and month_today > month_due) or (year_today == year_due and month_today == month_due and day_today > day_due):
            answer.append(i + 1)
            
    return answer