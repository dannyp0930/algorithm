def solution(n):
    answer = []
    n = list(str(n))
    while n:
        answer.append(int(n.pop()))
    return answer
