N = int(input())
arr = list(map(int, input().split()))
ans = [0] * N
stack = []
for i in range(N - 1, -1, -1):
    while stack and stack[-1] <= arr[i]:
        stack.pop()
    if not stack:
        ans[i] = -1
    else:
        ans[i] = stack[-1]
    stack.append(arr[i])
print(*ans)
