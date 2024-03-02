for i in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))
    h, l = 0, 0

    for _ in range(dump):
        highest, lowest = max(box), min(box)
        for j in range(len(box)):
            if box[j] == highest:
                h = j
                break
        for j in range(len(box)):
            if box[j] == lowest:
                l = j
                break
        
        box[h] -= 1
        box[l] += 1
        
        if max(box) - min(box) == 0 or max(box) - min(box) == 1:
            print("#{} {}".format(i, max(box) - min(box)))
            break
              
    print("#{} {}".format(i, max(box) - min(box)))