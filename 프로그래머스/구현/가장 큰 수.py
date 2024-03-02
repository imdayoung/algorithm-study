def solution(numbers):
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    numbers.sort(key = lambda x:x*3, reverse = True)
    return str(int(''.join(num for num in numbers)))