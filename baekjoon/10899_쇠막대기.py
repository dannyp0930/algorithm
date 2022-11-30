bar = input()
ans = 0
stack = []
for i in range(len(bar)):
    if bar[i] == ')':
        stack.pop()
        if bar[i - 1] == '(':
            ans += len(stack)
        else:
            ans += 1
    else:
        stack.append(bar[i])
print(ans)
