import sys
sys.stdin = open('2819.txt', 'r')

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def dfs(r, c, tmp):
    tmp += arr[r][c]
    if len(tmp) == 7:
        lst.add(tmp)
        return
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, tmp)


for T in range(1, int(input()) + 1):
    arr = [list(map(str, input().split())) for _ in range(4)]
    lst = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, '')
    print('#{} {}'.format(T, len(lst)))
