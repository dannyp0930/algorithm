from collections import deque


N, M = map(int, input().split())
arr = list(map(int, input().split()))
dq = deque([i for i in range(1, N + 1)])
cnt = 0
for n in arr:
    if dq.index(n) < len(dq) / 2:
        while dq[0] != n:
            dq.append(dq.popleft())
            cnt += 1
    else:
        while dq[0] != n:
            dq.appendleft(dq.pop())
            cnt += 1
    dq.popleft()
print(cnt)
