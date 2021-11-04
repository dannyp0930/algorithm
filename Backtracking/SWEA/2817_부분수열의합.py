import sys
sys.stdin = open('2817.txt', 'r')


def dfs(n):
    global tot, cnt
    if tot > K:
        return
    if tot == K:
        cnt += 1
        return
    for i in range(n, N):
        tot += arr[i]
        dfs(i + 1)
        tot -= arr[i]


for T in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    tot = 0
    cnt = 0
    dfs(0)
    print('#{} {}'.format(T, cnt))
