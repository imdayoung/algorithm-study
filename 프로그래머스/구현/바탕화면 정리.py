def solution(wallpaper):
    left, right, top, bottom = 0, 0, 0, 0
    row = len(wallpaper[0])
    col = len([i[0] for i in wallpaper])
    answer = []
    
    # top
    for i in range(col):
        if "#" in wallpaper[i]:
            top = i
            break
    #left
    for i in range(row):
        if "#" in [j[i] for j in wallpaper]:
            left = i
            break
    # bottom
    for i in range(col - 1, -1, -1):
        if "#" in wallpaper[i]:
            bottom = i + 1
            break
    # right
    for i in range(row - 1, -1, -1):
        if "#" in [j[i] for j in wallpaper]:
            right = i + 1
            break
            
    return [top, left, bottom, right]