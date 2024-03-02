def solution(arr1, arr2):
    n_arr1 = len([a[0] for a in arr1])
    l = len(arr1[0])
    m_arr2 = len(arr2[0])
    
    answer = [[0 for _ in range(m_arr2)] for _ in range(n_arr1)]
    arr2_rev = [[a[i] for a in arr2] for i in range(m_arr2)]

    for i in range(n_arr1):
        for j in range(m_arr2):
            temp = 0
            for k in range(l):
                temp += arr1[i][k] * arr2_rev[j][k]
            answer[i][j] = temp
        
    return answer