import heapq


n, m = map(int, input().split())
arr = list(map(int, input().split()))
heapq.heapify(arr)
while m:
    a, b = heapq.heappop(arr), heapq.heappop(arr)
    heapq.heappush(arr, a + b)
    heapq.heappush(arr, a + b)
    m -= 1
print(sum(arr))
