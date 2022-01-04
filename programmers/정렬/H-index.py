def solution(citations):
    n = len(citations)
    for h in range(n, -1, -1):
        cnt = 0
        for c in citations:
            if c >= h:
                cnt += 1
        if cnt >= h >= n - cnt:
            return h
