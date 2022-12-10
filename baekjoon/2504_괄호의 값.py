s = input()
stack = []
ans = 0
tmp = 1
for i, ch in enumerate(s):
    if ch == '(':
        stack.append(ch)
        tmp *= 2
    elif ch == '[':
        stack.append(ch)
        tmp *= 3
    elif ch == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if s[i - 1] == '(':
            ans += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if s[i - 1] == '[':
            ans += tmp
        stack.pop()
        tmp //= 3
if stack:
    ans = 0
print(ans)
