import sys
sys.stdin = open('1949.txt', 'r')

# 시계방향
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def boundary(a, b):
    return 0 <= a < N and 0 <= b < N and not visited[a][b]


# 1. 현재 위치를 들고 다니지 않을 때
# r, c : 좌표, road : 조성된 등산로 길이, skill : 공사 여부
def work(r, c, road, skill):
    global ans
    if road > ans:
        ans = road
    visited[r][c] = 1
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if boundary(nr, nc):
            # 현 위치보다 낮은 곳으로 이동
            if mountain[r][c] > mountain[nr][nc]:
                work(nr, nc, road + 1, skill)
            # 현 위치보다 높거나 같은 곳으로 이동
            elif skill and mountain[r][c] > mountain[nr][nc] - K:
                tmp = mountain[nr][nc]  # 기록
                mountain[nr][nc] = mountain[r][c] - 1
                work(nr, nc, road + 1, 0)   # 스킬 사용
                mountain[nr][nc] = tmp
    visited[r][c] = 0


# 2. 현재위치 들고 다닐 때
def work2(r, c, h, road, skill):
    global ans
    if road > ans:
        ans = road
    visited[r][c] = 1
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if not boundary(nr, nc):
            continue
        if h > mountain[nr][nc]:
            work2(nr, nc, mountain[nr][nc], road + 1, skill)
        elif skill and h > mountain[nr][nc] - K:
            work2(nr, nc, mountain[r][c] - 1, road + 1, 0)
    visited[r][c] = 0


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = []
    max_h = 0
    for i in range(N):
        tmp = list(map(int, input().split()))
        for val in tmp:
            if max_h < val:
                max_h = val
        mountain.append(tmp)
    visited = [[0] * N for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if max_h == mountain[i][j]:
                # work(i, j, 1, 1)    # 좌표, 길, 스킬
                work2(i, j, max_h, 1, 1)    # 좌표, 높이, 길, 스킬
    print('#{} {}'.format(tc, ans))
