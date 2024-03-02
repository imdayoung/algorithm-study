import copy


def cal(op, a, b):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    return a * b


def cal_priority(exp_num, exp_op, op):
    i = 0
    while i < len(exp_op):
        if exp_op[i] == op:
            exp_num.insert(i, cal(exp_op[i], exp_num[i], exp_num[i + 1]))
            del exp_num[i + 1]
            del exp_num[i + 1]
            del exp_op[i]
        else:
            i += 1

    return exp_num, exp_op


def solution(expression):
    operations = [('+', '-', '*'), ('+', '*', '-'), ('*', '+', '-'), ('*', '-', '+'), ('-', '*', '+'), ('-', '+', '*')]
    answer = 0

    exp_num = []
    exp_op = []
    num = ''
    for i in range(len(expression)):
        temp = expression[i]
        if temp.isdigit():
            num += temp
        else:
            exp_num.append(int(num))
            exp_op.append(temp)
            num = ''

        if i == len(expression) - 1:
            exp_num.append(int(num))

    for operation in operations:
        op1, op2 = operation[0], operation[1]

        new_exp_num = copy.deepcopy(exp_num)
        new_exp_op = copy.deepcopy(exp_op)

        new_exp_num, new_exp_op = cal_priority(new_exp_num, new_exp_op, op1)
        new_exp_num, new_exp_op = cal_priority(new_exp_num, new_exp_op, op2)

        final = ''
        for i in range(len(new_exp_op)):
            final += str(new_exp_num[i]) + new_exp_op[i]
        final += str(new_exp_num[-1])

        answer = max(answer, abs(eval(final)))

    return answer