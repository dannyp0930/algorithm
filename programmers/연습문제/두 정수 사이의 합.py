def solution(a, b):
    answer = 0
    for n in range(min(a, b), max(a, b) + 1):
        answer += n
    return answer
