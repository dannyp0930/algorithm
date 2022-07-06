def LIS(arr):
    if not arr:
        return 0
    l = len(arr)
    dp = [1] * l
    for i in range(1, l):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return dp


N = int(input())
A = list(map(int, input().split()))

left = LIS(A)
right = LIS(A[::-1])[::-1]
result = [left[i] + right[i] - 1 for i in range(N)]
print(max(result))
