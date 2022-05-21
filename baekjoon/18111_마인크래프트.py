import sys


N, M, B = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 최대 높이, 최소 높이
max_h, min_h = max(map(max, arr)), min(map(min, arr))
time = 256 * N * M
height = 0
# 목표 높이의 후보
for h in range(min_h, max_h + 1):
    high = 0
    low = 0
    for r in range(N):
        for c in range(M):
            # 목표 높이 보다 높다면 1번 수행
            if arr[r][c] > h:
                high += arr[r][c] - h
            # 목표 높이 보다 낮다면 2번 수행
            else:
                low += h - arr[r][c]
    # 인벤토리 조건
    if B + high < low: continue
    t = 2 * high + low
    if time >= t:
        time, height = t, h
print(time, height)
