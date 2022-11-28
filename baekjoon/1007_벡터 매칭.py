import sys


def comb(idx):
    global ans
    if len(stack) == N // 2:
        x, y = 0, 0
        for i in range(N):
            if i in stack:
                x += P[i][0]
                y += P[i][1]
            else:
                x -= P[i][0]
                y -= P[i][1]
        ans = min(ans, (x ** 2 + y ** 2) ** 0.5)
        return
    for i in range(idx, N):
        if i in stack: continue
        stack.append(i)
        comb(i)
        stack.pop()


input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    stack = []
    ans = 0xfffffff
    comb(0)
    print(ans)