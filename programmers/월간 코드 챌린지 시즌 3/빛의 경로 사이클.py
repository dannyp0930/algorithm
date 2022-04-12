dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def solution(grid):
    global visit, R, C
    R = len(grid)
    C = len(grid[0])
    answer = []
    visit = [[[0] * 4 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            for d in range(4):
                if not visit[r][c][d]:
                    length = light(r, c, d, grid)
                    if length:
                        answer.append(length)
    return sorted(answer)


def light(sr, sc, sd, grid):
    global visit
    r, c, d = sr, sc, sd
    cnt = 0
    visit[sr][sc][sd] = 1
    while 1:
        r, c = (r + dr[d]) % R, (c + dc[d]) % C
        cnt += 1
        if grid[r][c] == "R":
            d = (d + 1) % 4
        elif grid[r][c] == "L":
            d = (d - 1) % 4
        if visit[r][c][d]:
            if (r, c, d) == (sr, sc, sd):
                return cnt
            else:
                return 0
        visit[r][c][d] = 1
