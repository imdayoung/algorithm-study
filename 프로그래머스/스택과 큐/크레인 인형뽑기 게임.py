def solution(board, moves):
    answer = 0
    basket = []

    for j in moves:
        for i in range(len(board)):
            if [a[j - 1] for a in board][i] != 0:
                if len(basket) > 0 and basket[-1] == [a[j - 1] for a in board][i]:
                    basket.pop()
                    answer += 2
                else:
                    basket.append([a[j - 1] for a in board][i])
                board[i][j - 1] = 0
                break

    return answer