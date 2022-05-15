import sys
sys.stdin = open('2814.txt', 'r')


def dfs(v, cnt):
    global result
    visit[v] = 1
    if result < cnt:    # 최댓값인 경우에 저장
        result = cnt
    for w in range(1, N + 1):
        if arr[v][w] and not visit[w]:
            dfs(w, cnt + 1)
            visit[w] = 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    # N : 정점 , M : 간선  
    arr = [[0] * (N + 1) for _ in range(N + 1)] # 정보 저장을 위한 그래프
    stack = [0]
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a][b] = arr[b][a] = 1   # 정보 저장
    result = 0
    for i in range(1, N + 1):   # 모든 정점을 시작점으로 하여 계산
        visit = [0] * (N + 1)
        dfs(i, 1)
    print('#{} {}'.format(tc, result))
