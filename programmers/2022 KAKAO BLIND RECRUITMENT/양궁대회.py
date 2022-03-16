from itertools import combinations_with_replacement


def solution(n, info):
    answer = [-1]
    max_score_difference = 0
    for candi in combinations_with_replacement(range(11), n):
        lion = [0] * 11
        for t in candi:
            lion[t] += 1
        lion = lion[::-1]
        appeach_score, lion_score = 0, 0
        for i in range(11):
            score = 10 - i
            if info[i] >= lion[i] and info[i]:
                appeach_score += score
            elif info[i] < lion[i]:
                lion_score += score
        if appeach_score < lion_score:
            score_difference = lion_score - appeach_score
            if max_score_difference < score_difference:
                max_score_difference = score_difference
                answer = lion[:]
    return answer
