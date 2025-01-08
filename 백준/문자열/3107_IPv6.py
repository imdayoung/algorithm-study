def append_nums(nums):
    temp = ""
    
    for num in nums:
        if (len(num)) == 4:
            temp += num + ":"
        else:
            temp += "0" * (4 - len(num)) + num + ":"
            
    return temp


answer = ""

ip_address = input()
temp = list(ip_address.split("::"))

# :: 없음
if len(temp) == 1:
    nums = list(temp[0].split(":"))
    answer += append_nums(nums)

# :: 있음
else:
    if temp[0] == '':
        nums = list(temp[1].split(":"))
        answer += "0000:" * (8 - len(nums))
        answer += append_nums(nums)
        
    elif temp[1] == '':
        nums = list(temp[0].split(":"))
        answer += append_nums(nums)
        answer += "0000:" * (8 - len(nums))
        
    else:
        temp1 = list(temp[0].split(":"))
        temp2 = list(temp[1].split(":"))
        answer += append_nums(temp1)
        answer += "0000:" * (8 - len(temp1) - len(temp2))
        answer += append_nums(temp2)

print(answer[:-1])
