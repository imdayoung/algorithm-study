dic = {"0001101":0, "0011001":1, "0010011":2, "0111101":3, "0100011":4, "0110001":5,"0101111":6, "0111011":7, "0110111":8, "0001011":9}

T = int(input())
for tc in range(1, T + 1):
    code = ""
    N, M = map(int, input().split())
    for i in range(N):
        temp = list(map(str, input()))
        # 1이 포함되어 있으면 코드에 해당 input 저장
        if "1" in temp and not code:
            code = ''.join(temp)
            # 마지막 1의 위치 확인 및 저장
            for i in range(-1, -M, -1):
                if code[i] == "1":
                    end = i
                    break
    
    nums = []
    code = code[end - 55:end + 1]                
    for i in range(0, 50, 7):
        binary = code[i:i + 7]
        nums.append(dic[binary])
    
    check = 0
    for i in range(8):
        if i % 2 == 0:
            check += nums[i] * 3
        else:
            check += nums[i]

    if check % 10 == 0:
        answer = sum(nums)
    else:
        answer = 0

    print(f"#{tc} {answer}")