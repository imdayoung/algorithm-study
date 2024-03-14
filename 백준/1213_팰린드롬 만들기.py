name = list(map(str, input()))
name.sort()
n = len(name)
dict = {}
for char in name:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

answer = [0 for _ in range(n)]
idx = 0
for key in dict:
    while dict[key] > 0:
        if dict[key] % 2 == 0:
            answer[idx] = key
            answer[n - 1 - idx] = key
            dict[key] -= 2
            idx += 1
        else:
            if answer[n // 2] != 0:
                print("I'm Sorry Hansoo")
                exit()
      
            answer[n // 2] = key
            dict[key] -= 1

print(''.join(i for i in answer))