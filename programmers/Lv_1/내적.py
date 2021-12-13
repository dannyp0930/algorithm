def solution(a, b):
    answer = 0
    for na, nb in zip(a, b):
        answer += na * nb
    return answer
