N, K = map(int, input().split())
arr = list(map(int, input().split()))
tmp = sum(arr[:K])
ans = tmp
for i in range(N - K):
    tmp += (arr[i + K] - arr[i])
    ans = max(ans, tmp)
print(ans)