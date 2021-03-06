import sys
sys.stdin = open('3307.txt', 'r')

for T in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [1] * N
    for i in range(1, N):
        for j in range(i):
            if arr[i] >= arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    print('#{} {}'.format(T, max(dp)))
