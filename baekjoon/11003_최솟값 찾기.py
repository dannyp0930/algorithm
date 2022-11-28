from collections import deque
import sys

input = sys.stdin.readline
N, L = map(int, input().split())
arr = list(map(int, input().split()))
ans = [0] * N
dq = deque()
for i in range(N):
    while dq and dq[-1][0] > arr[i]:
        dq.pop()
    while dq and dq[0][1] < i - L + 1:
        dq.popleft()
    dq.append((arr[i], i))
    ans[i] = dq[0][0]
print(*ans)
