import sys, heapq

input = sys.stdin.readline
N, K = map(int, input().split())
jewels= [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
jewels.sort()
bags.sort()
ans = 0
heap = []
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(heap, -jewels[0][1])
        heapq.heappop(jewels)
    if heap:
        ans -= heapq.heappop(heap)
    elif not jewels:
        break
print(ans)