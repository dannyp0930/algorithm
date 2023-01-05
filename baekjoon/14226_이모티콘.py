from collections import deque


S = int(input())
q = deque([(1, 0)])
visit = [[-1] * (S + 1) for _ in range(S + 1)]
visit[1][0] = 0
while q:
    s, c = q.popleft()
    # 1
    if visit[s][s] == -1:
        visit[s][s] = visit[s][c] + 1
        q.append((s, s))
    # 2.
    if s + c <= S and visit[s + c][s] == -1:
        visit[s + c][c] = visit[s][c] + 1
        q.append((s + c, c))
    # 3.
    if s and visit[s - 1][c] == -1:
        visit[s - 1][c] = visit[s][c] + 1
        q.append((s - 1, c))
print(min([t for t in visit[S] if t != -1]))
