def solution(brown, yellow):
    height = 0
    width = (brown + 4) // 2 - height
    while (width * height) != (brown + yellow):
        width -= 1
        height += 1
    return [width, height]