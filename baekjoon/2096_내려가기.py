import sys

input = sys.stdin.readline
N = int(input())
max_dp = [0] * 3
min_dp = [0] * 3
for _ in range(N):
    num = list(map(int, input().split()))
    max_dp = [
        max(max_dp[0], max_dp[1]) + num[0],
        max(max_dp[0], max_dp[1], max_dp[2]) + num[1],
        max(max_dp[1], max_dp[2]) + num[2]
    ]
    min_dp = [
        min(min_dp[0], min_dp[1]) + num[0],
        min(min_dp[0], min_dp[1], min_dp[2]) + num[1],
        min(min_dp[1], min_dp[2]) + num[2]
    ]
print(max(max_dp), min(min_dp))
