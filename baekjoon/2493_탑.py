N = int(input())
arr = list(map(int, input().split()))
ans = []
stack = []
for i, t in enumerate(arr):
    while stack:
        if stack[-1][1] > t:
            ans.append(stack[-1][0])
            break
        else:
            stack.pop()
    if not stack:
        ans.append(0)
    stack.append((i + 1, t))
print(*ans)
