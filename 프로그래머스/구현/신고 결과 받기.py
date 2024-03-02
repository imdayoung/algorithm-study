def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported_id_dic = {}
    
    for i in id_list:
        reported_id_dic[i] = 0
        
    report_set = set(report)
    for report in report_set:
        reported_id_dic[report.split()[1]] += 1
    
    for i in id_list:
        if reported_id_dic[i] < k:
            del reported_id_dic[i]
        
    for i in range(len(id_list)):
        for rid in reported_id_dic:
            if id_list[i]+" "+rid in report_set:
                answer[i] += 1
    return answer