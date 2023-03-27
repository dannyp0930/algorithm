import heapq


N = int(input())
num = -int(input())
if N == 1:
    print(0)
else:
    arr = [-int(input()) for _ in range(N - 1)]
    ans = 0
    heapq.heapify(arr)
    while arr[0] <= num:
        vote = heapq.heappop(arr)
        num -= 1
        vote += 1
        ans += 1
        heapq.heappush(arr, vote)
    print(ans)
