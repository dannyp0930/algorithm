from re import L
import sys
import heapq

input = sys.stdin.readline
for _ in range(int(input())):
    k = int(input())
    min_heap = []
    max_heap = []
    visit = [0] * k
    for i in range(k):
        ch, n = input().split()
        n = int(n)
        if ch == 'I':
            heapq.heappush(min_heap, (n, i))
            heapq.heappush(max_heap, (-n, i))
            visit[i] = 1
        else:
            if n == 1:
                while max_heap and not visit[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)
            else:
                while min_heap and not visit[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visit[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    if min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
