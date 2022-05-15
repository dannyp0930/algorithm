def dfs(cnt):
    global result
    if len(start) == N // 2:
        start_abil = 0
        link_abil = 0
        for i in range(N):
            if i not in start:
                link.append(i)
        for j in range(N // 2 - 1):
            for k in range(j + 1, N // 2):
                start_abil += arr[start[j]][start[k]] + arr[start[k]][start[j]]
                link_abil += arr[link[j]][link[k]] + arr[link[k]][link[j]]
        diff = abs(start_abil - link_abil)
        result = min(result, diff)
        link.clear()
        return

    for i in range(cnt, N):
        start.append(i)
        dfs(i + 1)
        start.pop()


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
start = []
link = []
result = 100 * N
dfs(0)
print(result)
