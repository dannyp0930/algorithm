from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for candi in permutations(dungeons, len(dungeons)):
        tmp = 0
        p = k
        for t in candi:
            if p >= t[0]:
                p -= t[1]
                tmp += 1
        if answer < tmp:
            answer = tmp
    return answer
