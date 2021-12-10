def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    minimum = 0
    unknown = 0
    for lotto in lottos:
        if lotto in win_nums:
            minimum += 1
        if not lotto:
            unknown += 1
    maximum = minimum + unknown
    answer = [rank[maximum], rank[minimum]]
    return answer
