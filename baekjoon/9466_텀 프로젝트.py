import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def dfs(u):
    global ans
    visit[u] = 1
    cycle.append(u)
    v = arr[u]
    if not visit[v]:
        dfs(v)
    else:
        if v in cycle:
            for i in range(len(cycle)):
                if cycle[i] == v:
                    ans -= len(cycle[i:])
                    return
        return

for _ in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visit = [0] * (n + 1)
    ans = n
    for i in range(1, n + 1):
        if not visit[i]:
            cycle = []
            dfs(i)
    print(ans)
