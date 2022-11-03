N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
cnt = max(dp)
print(cnt)
res = []
for i in range(N - 1, -1, -1):
    if dp[i] == cnt:
        res.append(arr[i])
        cnt -= 1
res.reverse()
print(*res)
