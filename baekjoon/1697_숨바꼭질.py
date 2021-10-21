# 백트래킹

N, K = map(int, input().split())
visit = [0] * 100001
Q = [0] * 100001    # 선형 큐 사용
front, rear = -1, 0
Q[rear] = N
visit[N] = 1
while Q:
    front += 1
    x = Q[front]
    Q[front] = 0
    if x == K:
        break
    for nx in (x + 1, x - 1, 2 * x):
        if 0 <= nx < 100001 and not visit[nx]:
            visit[nx] = visit[x] + 1
            rear += 1
            Q[rear] = nx
print(visit[K] - 1)
