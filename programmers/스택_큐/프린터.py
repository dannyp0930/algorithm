def solution(priorities, location):
    answer = 0
    Q = [(i, p) for i, p in enumerate(priorities)]
    while 1:
        cur = Q.pop(0)
        if any(cur[1] < q[1] for q in Q):
            Q.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
