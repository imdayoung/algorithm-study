# count = 0
# n, k = map(int, input().split())

# while bin(n).count('1') > k:
#     count += 1
#     n += 1

# print(count)

# bin 대신 format 함수 사용하면 앞에 0X 붙지 않음 꿀팁
N, K = map(int, input().split())
answer = 0

while True:
    bin_n = format(N, 'b')
    if K >= bin_n.count('1'):
        break
    answer += 1
    N += 1
    
print(answer)