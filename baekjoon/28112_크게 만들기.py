N, K = map(int, input().split())
num = input()
stack = []
for n in num:
    while stack and K and stack[-1] < n:
        stack.pop()
        K -= 1
    stack.append(n)
if K:
    print(''.join(stack[:-K]))
else:
    print(''.join(stack))
