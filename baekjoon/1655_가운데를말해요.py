from heapq import heappop, heappush
import sys


input = sys.stdin.readline
min_heap = []
max_heap = []
for _ in range(int(input())):
    n = int(input())
    if len(max_heap) == len(min_heap):
        heappush(max_heap, -n)
    else:
        heappush(min_heap, n)
    if not min_heap:
        print(-max_heap[0])
        continue
    if -max_heap[0] > min_heap[0]:
        a = -heappop(min_heap)
        b = -heappop(max_heap)
        heappush(max_heap, a)
        heappush(min_heap, b)
    print(-max_heap[0])
