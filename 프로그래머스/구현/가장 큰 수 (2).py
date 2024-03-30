def solution(numbers):
    temp = [str(number) * 3 for number in numbers]
    temp.sort(reverse = True)
    answer_temp1 = str(int(''.join(i[:len(i) // 3] for i in temp)))
    return answer_temp1


print(solution([6, 10, 2]))
# 6210
print(solution([3, 30, 34, 5, 9]))
# 9534330
print(solution([19, 991, 9]))