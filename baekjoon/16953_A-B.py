import sys

input = sys.stdin.readline
A, B = map(int, input().split())
ans = -1
queue = [(A, 1)]
while queue:
    n, t = queue.pop(0)
    if n > B: continue
    if n == B:
        ans = t
        break
    queue.append((n * 2, t + 1))
    queue.append((n * 10 + 1, t + 1))
print(ans)
