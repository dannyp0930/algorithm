import heapq


def solution(n, works):
    if sum(works) <= n:
        return 0
    works = [-w for w in works]
    heapq.heapify(works)
    while n:
        heapq.heappush(works, heapq.heappop(works) + 1)
        n -= 1
    return sum([w * w for w in works])