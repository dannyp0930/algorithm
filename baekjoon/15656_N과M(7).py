def perm(cnt):
    if len(stack) == M:
        print(*stack)
        return
    for i in range(N):
        stack.append(arr[i])
        perm(cnt + 1)
        stack.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
stack = []
perm(0)
