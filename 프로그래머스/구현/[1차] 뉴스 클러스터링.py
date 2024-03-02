from collections import Counter
import copy


def get_set(s):
    s = s.upper()
    mul_set = []
    for i in range(len(s) - 1):
        temp = s[i:i + 2]
        if temp.isalpha():
            mul_set.append(temp)
    return mul_set


def solution(str1, str2):
    str1_set = get_set(str1)
    str2_set = get_set(str2)
    if len(str1_set) + len(str2_set) == 0:
        return 65536

    inter_set_temp = list(set(str1_set) & set(str2_set))
    str1_counter = Counter(str1_set)
    str2_counter = Counter(str2_set)

    # 교집합, 합집합 구하기
    inter_set = copy.deepcopy(inter_set_temp)
    union_set = []
    for i in inter_set_temp:
        inter_set += [i] * (min(str1_counter[i], str2_counter[i]) - 1)
        union_set += [i] * (max(str1_counter[i], str2_counter[i]))
    
    for s in str1_set:
        if s not in inter_set_temp:
            union_set.append(s)
    for s in str2_set:
        if s not in inter_set_temp:
            union_set.append(s)
    
    return int((len(inter_set) / len(union_set)) * 65536)