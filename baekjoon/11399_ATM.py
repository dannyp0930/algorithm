import sys

input = sys.stdin.readline
N = int(input())
P = sorted(list(map(int, input().split())))
ans = 0
for i in range(N):
    ans += (N - i) * P[i]
print(ans)
