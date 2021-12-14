from itertools import combinations


def solution(numbers):
    answer = []
    for i in combinations(numbers, 2):
        num = sum(i)
        if num in answer: continue
        answer.append(num)
    answer.sort()
    return answer
