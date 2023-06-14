import sys


input = sys.stdin.readline
N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]
s = 0
ans = 0
while s < N:
    test = arr[s: s + k]
    if s + k >= N:
        test += arr[: s + k - N]
    test = set(test)
    cnt = len(test)
    if not c in test:
        cnt += 1
    ans = max(ans, cnt)
    s += 1
print(ans)
