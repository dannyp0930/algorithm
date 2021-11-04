dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dfs(x, y):
    if len(tmp) == 6:
        num_set.add(''.join(str(tmp)))
        return
    for d in range(4):
        nx, ny = x + dr[d], y + dc[d]
        if 0 <= nx < 5 and 0 <= ny < 5:
            tmp.append(arr[nx][ny])
            dfs(nx, ny)
            tmp.pop()


arr = [list(map(int, input().split())) for _ in range(5)]
num_set = set()
for i in range(5):
    for j in range(5):
        tmp = [arr[i][j]]
        dfs(i, j)
print(len(num_set))
