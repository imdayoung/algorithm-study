def solution(prices):
    answer = {}
    stack = []
    
    prices = list(enumerate(prices))
    stack.append(prices[0])
    for i in range(1, len(prices)):
        temp = prices[i]
        while stack:
            if stack[-1][1] > temp[1]:
                answer[stack[-1][0]] = temp[0] - stack[-1][0]
                stack.pop()
            else:
                break
        stack.append(temp)
        
    for i in range(len(prices)):
        if i not in answer:
            answer[i] = len(prices) - i - 1
            
    return [answer[i] for i in range(len(answer))]