import sys
sys.stdin = open('4012.txt', 'r')


def synergy(lst):
    result = 0
    for i in range(N // 2 - 1):
        for j in range(i + 1, N // 2):
            result += arr[lst[i]][lst[j]] + arr[lst[j]][lst[i]]
    return result


def dfs(idx, k):
    global ans
    if idx == N // 2:
        a = []
        b = []
        for j in range(N):
            if visited[j]:
                a.append(j)
            else:
                b.append(j)
        syn_a = synergy(a)
        syn_b = synergy(b)
        if ans > abs(syn_a - syn_b):
            ans = abs(syn_a - syn_b)
        return
    for i in range(k, N):
        if not visited[i]:
            visited[i] = 1
            dfs(idx + 1, i + 1)
            visited[i] = 0


for T in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    visited[0] = 1
    ans = 19999 * (N // 2)
    dfs(1, 1)
    print('#{} {}'.format(T, ans))
