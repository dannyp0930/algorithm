N = int(input())
K = int(input())
arr = list(map(int, input().split()))
if K >= N:
    print(0)
else:
    arr.sort()
    dist = [0] * (N - 1)
    for i in range(N - 1):
        dist[i] = arr[i + 1] - arr[i]
    dist.sort()
    for _ in range(K - 1):
        dist.pop()
    print(sum(dist))
