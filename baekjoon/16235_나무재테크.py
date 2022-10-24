def spring_summer():
    global ans
    for r in range(N):
        for c in range(N):
            l = len(trees[r][c])
            for i in range(l):
                if trees[r][c][i] <= foods[r][c]:
                    foods[r][c] -= trees[r][c][i]
                    trees[r][c][i] += 1
                else:
                    for _ in range(i, l):
                        foods[r][c] += trees[r][c].pop() // 2
                        ans -= 1
                    break


def fall_winter():
    global ans
    for r in range(N):
        for c in range(N):
            l = len(trees[r][c])
            for i in range(l):
                if trees[r][c][i] % 5 == 0:
                    for d in range(8):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < N and 0 <= nc < N:
                            trees[nr][nc].insert(0, 1)
                            ans += 1
            foods[r][c] += A[r][c]


dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
foods = [[5] * N for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)
ans = M
for _ in range(K):
    spring_summer()
    fall_winter()
print(ans)
