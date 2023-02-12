import heapq


N = int(input())
q = []
for _ in range(N):
    arr = map(int, input().split())
    for num in arr:
        if len(q) < N:
            heapq.heappush(q, num)
        elif q[0] < num:
            heapq.heappop(q)
            heapq.heappush(q, num)
print(q[0])
