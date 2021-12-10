import sys
sys.stdin = open('1767.txt', 'r')

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dfs(idx, core, wire):
    global CORE, WIRE
    if idx == num_core:
        if CORE < core:
            CORE = core
            WIRE = wire
        elif CORE == core and WIRE > wire:
            WIRE = wire
        return
    r, c = cores[idx]
    # 4방 체크
    for d in range(4):
        # 방향 가능 여부 체크
        flag = 0
        nr, nc = r, c
        while 1:
            nr, nc = nr + dr[d], nc + dc[d]
            if nr < 0 or nc < 0 or nr >= N or nc >= N: break
            # 전선을 만나면
            if arr[nr][nc]: flag = 1; break
        if flag: continue
        nr, nc = r, c
        while 1:
            nr, nc = nr + dr[d], nc + dc[d]
            if nr < 0 or nc < 0 or nr >= N or nc >= N: break
            wire += 1
            arr[nr][nc] = 1
        dfs(idx + 1, core + 1, wire)
        nr, nc = r, c
        while 1:
            nr, nc = nr + dr[d], nc + dc[d]
            if nr < 0 or nc < 0 or nr >= N or nc >= N: break
            wire -= 1
            arr[nr][nc] = 0
    # 모든 방향이 불가능한 경우
    dfs(idx + 1, core, wire)


for T in range(1, int(input()) + 1):
    N = int(input())
    arr = []
    cores = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in range(1, N - 1):
            if i and i != N - 1 and tmp[j]:
                cores.append((i, j))
        arr.append(tmp)
    CORE = 0
    WIRE = N * N
    num_core = len(cores)
    dfs(0, 0, 0)
    print('#{} {}'.format(T, WIRE))
