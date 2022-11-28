import sys

def dfs(start, cnt):
    if cnt == M:
        print(*stack)
        return
    before = 0
    for i in range(N):
        if arr[i] != before:
            stack.append(arr[i])
            before = arr[i]
            dfs(i, cnt + 1)
            stack.pop()

input = sys.stdin.readline
N, M = map(int, input().split())
arr = sorted(list((map(int, input().split()))))
stack = []
dfs(0, 0)
