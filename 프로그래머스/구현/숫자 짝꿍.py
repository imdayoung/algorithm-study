def solution(X, Y):
    answer = ''
    X, Y = sorted(X, reverse = True), sorted(Y, reverse = True)
    for i in range(len(X)):
        X[i] = int(X[i])
    for i in range(len(Y)):
        Y[i] = int(Y[i])
    
    i, j = 0, 0
    while i < len(X) and j < len(Y):
        if X[i] == Y[j]:
            answer += str(X[i])
            i += 1
            j += 1
        elif X[i] < Y[j]:
            j += 1
        elif X[i] > Y[j]:
            i += 1
    return "-1" if answer == '' else "0" if answer[0] == "0" else answer