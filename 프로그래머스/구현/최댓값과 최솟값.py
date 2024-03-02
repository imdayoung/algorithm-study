def solution(s):
    nums_str = s.split()
    nums_int = [int(num) for num in nums_str]
    return str(min(nums_int)) + " " + str(max(nums_int))