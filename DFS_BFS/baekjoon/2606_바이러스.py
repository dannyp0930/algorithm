N = int(input())    # 컴퓨터 대수, 노드 수
E = int(input())    # 연결된 컴퓨터 쌍, 간선 수
arr = [[0] * (N + 1) for _ in range(N + 1)]     # 정보 저장을 위한 그래프
for _ in range(E):  # 정보 저장
    r, c = map(int, input().split())
    arr[r][c] = arr[c][r] = 1
visit = [0] * (N + 1)
v = 1
visit[v] = 1
stack = [0]
cnt = 0
while stack:
    for w in range(1, N + 1):
        if arr[v][w] == 1 and visit[w] == 0:
            stack.append(v)
            visit[w] = 1
            v = w
            cnt += 1
            break
    else:
        v = stack.pop()
print(cnt)
