from itertools import combinations

answer = []

l, c = map(int, input().split())
words = list(input().rstrip().split())

comb = list(combinations(words, l))

for pw in comb:
    pw = [i for i in pw]
    pw.sort()
    t = ''.join(pw)

    cnt_a, cnt_e, cnt_i, cnt_o, cnt_u = t.count("a"), t.count("e"), t.count("i"), t.count("o"), t.count("u")

    if (cnt_a > 0 or cnt_e > 0 or cnt_i > 0 or cnt_o > 0 or cnt_u > 0) and cnt_a + cnt_e + cnt_i + cnt_o + cnt_u <= l - 2:
        answer.append(t)

answer.sort()
for a in answer:
    print(a)