def perm(cnt):
    if cnt == M:
        print(*stack)
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            stack.append(arr[i])
            perm(cnt + 1)
            stack.pop()
            visit[i] = 0


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visit = [0] * N
stack = []
perm(0)
