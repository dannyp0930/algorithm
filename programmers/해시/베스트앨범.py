def solution(genres, plays):
    answer = []
    n = len(genres)
    genre_plays = dict()
    genre_id_plays = dict()
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in genre_plays:
            genre_plays[g] = p
        else:
            genre_plays[g] += p
        if g not in genre_id_plays:
            genre_id_plays[g] = [(i, p)]
        else:
            genre_id_plays[g].append((i, p))
    for k, v in sorted(genre_plays.items(), key=lambda x: -x[1]):
        for i, p in sorted(genre_id_plays[k], key=lambda x: -x[1])[:2]:
            answer.append(i)
    return answer
