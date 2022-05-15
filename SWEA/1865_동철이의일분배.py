import sys
sys.stdin = open('1865.txt', 'r')


def perm(idx):
    global result, tmp
    if idx == N:
        if result < tmp * 100:
            result = tmp * 100
        return
    if result > tmp * 100:
        return
    for i in range(N):
        if visit[i] or not P[idx][i]: continue
        visit[i] = 1
        tmp *= (P[idx][i] / 100)
        perm(idx + 1)
        visit[i] = 0
        tmp /= (P[idx][i] / 100)


for T in range(1, int(input()) + 1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    tmp = 1
    result = 0
    perm(0)
    print('#{} {:.6f}'.format(T, result))