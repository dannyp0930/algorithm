import sys
sys.stdin = open('10966.txt', 'r')

# from collections import deque
#
#
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
#
#
# def bfs():
#     while Q:
#         r, c = Q.popleft()
#         for k in range(4):
#             nr, nc = r + dr[k], c + dc[k]
#             if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == -1:
#                 Q.append((nr, nc))
#                 visit[nr][nc] = visit[r][c] + 1
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     visit = [[-1] * M for _ in range(N)]
#     Q = deque()
#     for i in range(N):
#         temp = input()
#         for j in range(M):
#             if temp[j] == 'W':
#                 Q.append((i, j))
#                 visit[i][j] = 0
#     bfs()
#     result = 0
#     for arr in visit:
#         for val in arr:
#             result += val
#     print('#{} {}'.format(tc, result))

##################################################
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visit = [[-1] * M for _ in range(N)]
    Q = [0] * (N * M)
    front, rear = -1, -1
    for i in range(N):
        temp = input()
        for j in range(M):
            if temp[j] == 'W':
                rear += 1
                Q[rear] = (i, j)
                visit[i][j] = 0
    while front != rear:
        front += 1
        r, c = Q[front]
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == -1:
                visit[nr][nc] = visit[r][c] + 1
                rear += 1
                Q[rear] = (nr, nc)
    result = 0
    for arr in visit:
        for val in arr:
            result += val
    print('#{} {}'.format(tc, result))
