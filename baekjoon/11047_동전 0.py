import sys

input = sys.stdin.readline
N, K = map(int, input().split())
coins = sorted([int(input()) for _ in range(N)], reverse=True)
cnt = 0
for coin in coins:
    if K >= coin:
        cnt += K // coin
        K %= coin
print(cnt)