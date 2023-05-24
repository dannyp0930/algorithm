dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


N = int(input())
target = int(input())
graph = [[0] * N for _ in range(N)]
r = c = 0
d = 0
num = N ** 2
x, y = 0, 0
if target == 1:
    x, y = N // 2 + 1, N // 2 + 1
while num != 0:
    graph[r][c] = num
    if num == target:
        x, y = r + 1, c + 1
    nr, nc = r + dr[d], c + dc[d]
    if nr == N // 2 and nc == N // 2:
        graph[nr][nc] = 1
        break
    if not (0 <= nr < N and 0 <= nc < N) or graph[nr][nc]:
        d = (d + 1) % 4
        continue
    r, c = nr, nc
    num -= 1

for lst in graph:
    print(*lst)
print(x, y)
