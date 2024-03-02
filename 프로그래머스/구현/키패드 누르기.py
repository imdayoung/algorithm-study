def solution(numbers, hand):
    answer = ''
    left, right = 10, 11
    
    num_dic = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], 10:[3,0], 0:[3,1], 11:[3,2]}
    
    for n in numbers:
        if n in [1, 4, 7]:
            answer += "L"
            left = n
        elif n in [3, 6, 9]:
            answer += "R"
            right = n
        else:
            l_dist = abs(num_dic[n][0] - num_dic[left][0]) + abs(num_dic[n][1] - num_dic[left][1])
            r_dist = abs(num_dic[n][0] - num_dic[right][0]) + abs(num_dic[n][1] - num_dic[right][1])
            if l_dist > r_dist or (l_dist == r_dist and hand == "right"):
                answer += "R"
                right = n
            else:
                answer += "L"
                left = n
            
    return answer