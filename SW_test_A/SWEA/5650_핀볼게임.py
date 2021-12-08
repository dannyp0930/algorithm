import sys
sys.stdin = open('5650.txt', 'r')


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

change = [
    [],
    [1, 3, 0, 2],
    [3, 0, 1, 2],
    [2, 0, 3, 1],
    [1, 2, 3, 0],
    [1, 0, 3, 2]
]


def start(r, c, d):
    score = 0
    origin = (r, c)
    while 1:
        r, c = r + dr[d], c + dc[d]
        if (r, c) == origin or arr[r][c] == -1:
            return score
        if 1 <= arr[r][c] <= 5:
            d = change[arr[r][c]][d]
            score += 1
        elif arr[r][c] > 5:
            r, c = wormhole[(r, c)]


for T in range(1, int(input()) + 1):
    N = int(input())
    arr = [[5] * (N + 2)]
    tmp = dict()
    wormhole = dict()
    for i in range(1, N + 1):
        lst = [5] + list(map(int, input().split())) + [5]
        for j in range(1, N + 1):
            if lst[j] >= 6:
                if lst[j] in tmp:
                    wormhole[tmp[lst[j]]] = (i, j)
                    wormhole[(i, j)] = tmp[lst[j]]
                else:
                    tmp[lst[j]] = (i, j)
        arr.append(lst)
    arr.append([5] * (N + 2))
    ans = 0
    for sr in range(1, N + 1):
        for sc in range(1, N + 1):
            if not arr[sr][sc]:
                for sd in range(4):
                    ans = max(ans, start(sr, sc, sd))
    print('#{} {}'.format(T, ans))
