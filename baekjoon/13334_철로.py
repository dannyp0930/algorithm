import sys
import heapq
input = sys.stdin.readline


n = int(input())
arr = [sorted(list(map(int, input().split()))) for _ in range(n)]
arr.sort(key=lambda x: x[1])
d = int(input())
res = 0
heap = []
for h, o in arr:
    if o - h <= d:
        heapq.heappush(heap, h)
    while heap and heap[0] < o - d:
        heapq.heappop(heap)
    res = max(res, len(heap))
print(res)
