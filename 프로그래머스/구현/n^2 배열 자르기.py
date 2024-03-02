def get_rc(n, num):
    row, col = num // n, num % n - 1
    if col == -1:
        row -= 1
        col = n - 1
    return row, col


def solution(n, left, right):
    l_row, l_col = get_rc(n, left + 1)
    r_row, r_col = get_rc(n, right + 1)
    
    arr = [[0 for _ in range(n)] for _ in range(r_row - l_row + 1)]
    for i in range(l_row, r_row + 1):
        for j in range(n - 1, -1, -1):
            if j <= i:
                arr[i - l_row][j] = i + 1
            else:
                arr[i - l_row][j] = j + 1
    
    if l_row == r_row:
        return arr[0][l_col:r_col + 1]
    else:
        temp = []
        for i in range(l_row, r_row + 1):
            if i == l_row:
                for j in arr[i - l_row][l_col:]:
                    temp.append(j)
            elif i == r_row:
                for j in arr[i - l_row][:r_col + 1]:
                    temp.append(j)
            else:
                for j in arr[i - l_row]:
                    temp.append(j)
        return temp


# # 1차 시간 초과
# def solution(n, left, right):
#     arr = []
#     for i in range(n):
#         for j in range(n):
#             arr.append(max(i + 1, j + 1))
            
#     return arr[left:right + 1]


# # 2차 시간 초과
# def solution(n, left, right):
#     arr = []
#     cnt = 0
    
#     for i in range(n):
#         for j in range(n):
#             if cnt >= left and cnt <= right:
#                 arr.append(max(i + 1, j + 1))
#             cnt += 1
            
#     return arr