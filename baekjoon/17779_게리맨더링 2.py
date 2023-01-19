def gerrymandering(x, y, d1, d2):
    global ans
    pop = [0] * 5
    tmp = [[0] * N for _ in range(N)]
    for i in range(d1 + 1):
        tmp[x + i][y - i] = 1
        tmp[x + d2 + i][y + d2 - i] = 1
    for i in range(d2 + 1):
        tmp[x + i][y + i] = 1
        tmp[x + d1 + i][y - d1 + i] = 1
    for i in range(x + 1, x + d1 + d2):
        flag = False
        for j in range(y - d1, y + d2 + 1):
            if tmp[i][j]:
                flag = not flag
            if flag:
                tmp[i][j] = 1
    for r in range(N):
        for c in range(N):
            if not tmp[r][c]:
                if r < x + d1 and c <= y:
                    pop[0] += arr[r][c]
                elif r <= x + d2 and y < c:
                    pop[1] += arr[r][c]
                elif x + d1 <= r and c < y - d1 + d2:
                    pop[2] += arr[r][c]
                elif x + d2 < r and y - d1 + d2 <= c:
                    pop[3] += arr[r][c]
            else:
                pop[4] += arr[r][c]
    ans = min(ans, max(pop) - min(pop))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 20000
for x in range(N):
    for y in range(N):
        for d1 in range(1, N + 1):
            for d2 in range(1, N + 1):
                if x + d1 + d2 < N and 0 <= y - d1 and y + d2 < N:
                    gerrymandering(x, y, d1, d2)
print(ans)
