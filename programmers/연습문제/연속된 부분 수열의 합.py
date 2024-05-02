def solution(sequence, k):
    answer = []
    s, e = 0, 0
    n = len(sequence)
    length = n + 1
    tot = sequence[0]
    while s <= e < n:
        if tot == k:
            if e - s + 1 < length:
                length = e - s + 1
                answer = [s, e]
            tot -= sequence[s]
            s += 1
        elif tot < k:
            e += 1
            if e < n:
                tot += sequence[e]
        else:
            tot -= sequence[s]
            s += 1
    return answer