def solution(n):
    cnt = format(n, "b").count("1")
    
    while True:
        n += 1
        if format(n, "b").count("1") == cnt:
            break
    return n