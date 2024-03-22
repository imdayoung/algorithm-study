def solution(genres, plays):
    n = len(plays)
    answer = []
    by_genre = {}
    genre_sum = {}
    for i in range(n):
        if genres[i] not in by_genre:
            by_genre[genres[i]] = [(i, plays[i])]
            genre_sum[genres[i]] = plays[i]
        else:
            by_genre[genres[i]] = by_genre[genres[i]] + [(i, plays[i])]
            genre_sum[genres[i]] += plays[i]
    sorted_genre = sorted(list(genre_sum.items()), key = lambda x:x[1], reverse = True)

    for i in range(len(sorted_genre)):
        selected_genre = sorted_genre[i][0]
        sorted_music_in_genre = sorted(by_genre[selected_genre], key = lambda x:-x[1])
        answer.append(sorted_music_in_genre[0][0])
        if len(sorted_music_in_genre) == 1:
            continue
        answer.append(sorted_music_in_genre[1][0])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
# [4, 1, 3, 0]