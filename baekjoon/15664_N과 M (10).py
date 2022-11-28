import sys

def dfs(start, cnt):
    if cnt == M:
        print(*stack)
        return
    before = 0
    for i in range(start, N):
        if not visit[i] and arr[i] != before:
            visit[i] = 1
            stack.append(arr[i])
            before = arr[i]
            dfs(i, cnt + 1)
            visit[i] = 0
            stack.pop()

input = sys.stdin.readline
N, M = map(int, input().split())
arr = sorted(list((map(int, input().split()))))
stack = []
visit = [0] * N
dfs(0, 0)
