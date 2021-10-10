dr = [-1, 0, 1, 0]
dc = [0, 1, -0, -1]


def clean(r, c, d):
    global ans
    if not arr[r][c]:   # 주어진 좌표가 청소할 수 있는 경우
        arr[r][c] = 2   # 청소 완료
        ans += 1        # 구역 개수 세기
    for _ in range(4):  # 방향 탐색
        nd = (d + 3) % 4    # 현재 방향의 왼쪽
        nr, nc = r + dr[nd], c + dc[nd]
        if not arr[nr][nc]: # 회전한 곳이 청소 할 수 있다면
            clean(nr, nc, nd)   # 청소 하기
            return
        d = nd  # 새로운 방향 설정
    nd = (d + 2) % 4    # 다 돌고 나왔는데 청소 할 수 없다면 뒤로 돌고
    nr, nc = r + dr[nd], c + dc[nd]
    if arr[nr][nc] == 1:    # 뒤로 돌았는데 벽이면
        return
    clean(nr, nc, d)    # 다시 청소 시작


N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
clean(r, c, d)
print(ans)
