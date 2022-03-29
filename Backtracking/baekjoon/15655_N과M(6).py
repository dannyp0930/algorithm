def comb(cnt):
    if len(stack) == M:
        print(*stack)
        return
    for i in range(cnt, N):
        stack.append(arr[i])
        comb(i + 1)
        stack.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
stack = []
comb(0)
