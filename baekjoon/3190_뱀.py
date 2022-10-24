def turn(S):
    global d
    if S == 'L':
        d = (d + 3) % 4
    else:
        d = (d + 1) % 4


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 2
L = int(input())
move = dict()
for _ in range(L):
    X, C = input().split()
    move[int(X)] = C
r, c = 0, 0
q = [(r, c)]
arr[r][c] = 1
d = 0
cnt = 0
while 1:
    cnt += 1
    r += dr[d]
    c += dc[d]
    if not (0 <= r < N and 0 <= c < N):
        break
    if arr[r][c] == 1:
        break
    if arr[r][c] == 0:
        tx, ty = q.pop(0)
        arr[tx][ty] = 0
    q.append((r, c))
    arr[r][c] = 1
    if cnt in move:
        turn(move[cnt])
print(cnt)
