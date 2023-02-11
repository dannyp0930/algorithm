ans = 0
for _ in range(int(input())):
    word = input()
    stack = []
    for ch in word:
        if stack and ch == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)
    if not stack:
        ans += 1
print(ans)
