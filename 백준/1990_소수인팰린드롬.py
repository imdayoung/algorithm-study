import sys


def get_palindrome(start, end):
    palindromes = []
    
    for num in range(start, end + 1):
        num = str(num)
        if (len(num) % 2 == 1 and num == num[::-1]) or num == "11":
            palindromes.append(int(num))
    
    return palindromes
    
    
def get_prime(nums):
    is_prime = []
    return is_prime
    

a, b = map(int, sys.stdin.readline().split())
palindromes = get_palindrome(a, b)
print(palindromes)

is_prime = get_prime(palindromes)
print(is_prime)


# get prime numbers가 단단히 잘못됨
# import sys


# def get_prime_numbers():
#     # MAX = 100000001
#     MAX = 1000000
#     is_prime = [True for _ in range(MAX)]
#     is_prime[0] = False
#     is_prime[1] = False
    
#     for i in range(2, int(MAX ** 0.5) + 1):
#         if is_prime[i]:
#             for j in range(i * 2, MAX, i):
#                 is_prime[j] = False
    
#     return is_prime
    

# a, b = map(int, sys.stdin.readline().split())
# prime_numbers = get_prime_numbers()
# print("End")
# for number in range(a, b + 1):
#     if prime_numbers[number]:
#         print(number)