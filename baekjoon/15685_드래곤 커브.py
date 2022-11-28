def rotate(x, y, xb, yb):
    return (yb - y + xb, x - xb + yb)


def sqaure(x, y):
    if graph[y][x + 1] and graph[y + 1][x] and graph[y + 1][x + 1]:
        return True
    return False


N = int(input())
graph = [[0] * 101 for _ in range(101)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    q = [(x, y), (x + dx[d], y + dy[d])]
    while 1:
        for i, j in q:
            if graph[j][i] == 0:
                graph[j][i] = 1
        if not g:
            break
        xb, yb = q[-1]
        n = len(q)
        for k in range(n - 2, -1, -1):
            x, y = q[k]
            nx, ny = rotate(x, y, xb, yb)
            if (nx, ny) not in q:
                q.append((nx, ny))
        g -= 1
ans = 0
for x in range(100):
    for y in range(100):
        if graph[y][x] and sqaure(x, y):
            ans += 1
print(ans)
