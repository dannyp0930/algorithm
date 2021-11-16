N = int(input())
population = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    tmp = list(map(int, input().split()))
    for j in range(1, tmp[0] + 1):
        graph[i].append(tmp[j])


def bfs(arr):
    Q = []
    visit = [0] * (N + 1)
    Q.append(arr[0])
    visit[arr[0]] = 1
    cnt, ans = 1, 0
    while Q:
        x = Q.pop(0)
        ans += population[x]
        for nx in graph[x]:
            if nx in arr and not visit[nx]:
                Q.append(nx)
                visit[nx] = 1
                cnt += 1
    if cnt == len(arr):
        return ans
    return 0


def comb(cnt, x, end):
    global result
    if cnt == end:
        arr1, arr2 = [], []
        for y in range(1, N + 1):
            if c[y]: arr1.append(y)
            else: arr2.append(y)
        ans1 = bfs(arr1)
        if not ans1: return
        ans2 = bfs(arr2)
        if not ans2: return
        result = min(result, abs(ans1 - ans2))
        return

    for m in range(x, N + 1):
        if c[m]: continue
        c[m] = 1
        comb(cnt + 1, m, end)
        c[m] = 0


result = 0xffffff
for n in range(1, N // 2 + 1):
    c = [0] * (N + 1)
    comb(0, 1, n)
if result == 0xffffff:
    print(-1)
else:
    print(result)
