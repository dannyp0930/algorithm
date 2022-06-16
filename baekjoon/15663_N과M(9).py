import sys


def perm(cnt):
    if cnt == M:
        print(*stack)
        return
    before = 0
    for i in range(N):
        if not visit[i] and arr[i] != before:
            visit[i] = 1
            stack.append(arr[i])
            before = arr[i]
            perm(cnt + 1)
            visit[i] = 0
            stack.pop()


input = sys.stdin.readline
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
stack = []
visit = [0] * N
perm_list = []
perm(0)
