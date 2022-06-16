import sys

def dfs(start, cnt):
    if cnt == M:
        print(*stack)
        return
    for i in range(start, N):
        stack.append(arr[i])
        dfs(i, cnt + 1)
        stack.pop()

input = sys.stdin.readline
N, M = map(int, input().split())
arr = sorted(list(set((map(int, input().split())))))
N = len(arr)
stack = []
dfs(0, 0)
