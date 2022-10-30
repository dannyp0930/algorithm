def solution(rectangle, characterX, characterY, itemX, itemY):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    coordinates = [[-1] * 101 for _ in range(101)]
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: 2 * x, r)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    coordinates[i][j] = 0
                elif coordinates[i][j] != 0:
                    coordinates[i][j] = 1
    q = [(characterX * 2, characterY * 2)]
    visit = [[0] * 101 for _ in range(101)]
    visit[characterX * 2][characterY * 2] = 1
    while q:
        x, y = q.pop(0)
        if x == itemX * 2 and y == itemY * 2:
            return visit[x][y] // 2
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if not (0 < nx < 101 and 0 < ny < 101):
                continue
            if coordinates[nx][ny] == 1 and visit[nx][ny] == 0:
                q.append((nx, ny))
                visit[nx][ny] = visit[x][y] + 1
