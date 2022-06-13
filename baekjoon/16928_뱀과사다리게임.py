import sys

input = sys.stdin.readline
N, M = map(int, input().split())
ladder = dict()
snake = dict()
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v
visit = [0] * 101
queue = [1]
while queue:
    now = queue.pop(0)
    for move in range(1, 7):
        check = now + move
        if 0 < check < 101 and not visit[check]:
            if check in ladder.keys():
                check = ladder[check]
            if check in snake.keys():
                check = snake[check]
            if not visit[check]:
                queue.append(check)
                visit[check] = visit[now] + 1
print(visit[100])
