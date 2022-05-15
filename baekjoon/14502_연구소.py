from itertools import combinations


N, M = map(int, input().split())
arr = []
# 바이러스 위치 저장
virus = []
# 현재 빈 곳의 위치 저장
space = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        if temp[j] == 0:
            space.append((i, j))
        elif temp[j] == 2:
            virus.append((i, j))
    arr.append(temp)

# 벽을 세울 수 있는 조합 생성
walls = list(combinations(space, 3))

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

ans = 0

# 후보 별로 test 진행
for wall in walls:
    # 원래 리스트 deepcopy
    test = [item[:] for item in arr]
    r1, c1 = wall[0]
    r2, c2 = wall[1]
    r3, c3 = wall[2]
    # 새로운 벽 건설
    test[r1][c1] = test[r2][c2] = test[r3][c3] = 1
    Q = virus[:]
    while Q:
        r, c = Q.pop(0)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nc < 0 or nr >= N or nc >= M: continue
            if test[nr][nc]: continue
            test[nr][nc] = 2
            Q.append((nr, nc))
    empty = 0
    for n in range(N):
        for m in range(M):
            if not test[n][m]:
                empty += 1
    if ans < empty:
        ans = empty
print(ans)
