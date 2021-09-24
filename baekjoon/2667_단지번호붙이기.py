# DFS/BFS

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:  # 지도 안에 있는지 확인
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            dfs(nx, ny)
        return True
    return False


n = int(input())    # 지도의 크기
graph = [list(map(int, input())) for _ in range(n)]     # 지도
num = []    # 단지별 집의 수
count = 0
result = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])
