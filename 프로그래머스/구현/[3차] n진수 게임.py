def to_n(x, n):
    dictionary = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',
                  10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

    d, m = divmod(x, n)
    x_to_n = dictionary[m]
    while d > 0:
        d, m = divmod(d, n)
        x_to_n = dictionary[m] + x_to_n

    return x_to_n


def solution(n, t, m, p):
    answer = ''
    nums_to_say = ""
    num = 0
    while len(nums_to_say) < t * m:
        nums_to_say += to_n(num, n)
        num += 1

    for i in range(p - 1, len(nums_to_say), m):
        answer += nums_to_say[i]
    return answer[:t]