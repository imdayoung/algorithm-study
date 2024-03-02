def solution(files):
    splited_files = []

    # 파일명을 HEAD, NUMBER, TAIL로 나누어 저장하기
    for file in files:
        head, number, tail = '', '', ''
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                break

        for i in range(len(number)):
            if not number[i].isdigit() or i > 5:
                tail = number[i:]
                number = number[:i]
                break

        splited_files.append((head, number, tail))

    splited_files.sort(key = lambda x:(x[0].lower(), int(x[1])))
    
    return [''.join(i) for i in splited_files]


# # 5~13, 16~20
# def solution(files):
#     answer = []
#     splited_files = []

#     for file in files:
#         head, number, tail = '', '', ''
#         is_head = True
#         zero_start = True
#         tail_start = len(file)
#         zero_cnt = 0
#         number_cnt = 0

#         for i in range(len(file)):
#             temp = file[i]
#             # HEAD에 추가할 수 있는 경우
#             if is_head and not temp.isdigit():
#                 head += temp

#             # 이제 HEAD가 아닌 NUMBER에 추가할 시간이 됨
#             elif is_head and temp.isdigit() and number_cnt < 5:
#                 is_head = False
#                 number += temp
#                 number_cnt += 1
#                 if temp != '0':
#                     zero_start = False
#                 else:
#                     zero_cnt += 1

#             # NUMBER에 추가할 수 있는 경우
#             elif not is_head and temp.isdigit() and number_cnt < 5:
#                 number += temp
#                 number_cnt += 1
#                 if zero_start and temp == '0':
#                     zero_cnt += 1
#                 else:
#                     zero_start = False
            
#             # 이제부터 TAIL에 추가
#             else:
#                 tail_start = i
#                 break

#         tail = file[tail_start:]
#         splited_files.append((head, int(number), tail, zero_cnt))
    
#     splited_files.sort(key = lambda x:(x[0].lower(), x[1]))
#     for head, number, tail, zero_cnt in splited_files:
#         answer.append(head + '0' * zero_cnt + str(number) + tail)

#     return answer

