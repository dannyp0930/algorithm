infix = input()
stack = []
postfix = ''
for ch in infix:
    if ch.isalpha():
        postfix += ch
    elif ch == '(':
        stack.append(ch)
    elif ch in ('*', '/'):
        while stack and stack[-1] in ('*', '/'):
            postfix += stack.pop()
        stack.append(ch)
    elif ch in ('+', '-'):
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        stack.append(ch)
    else:
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        stack.pop()
while stack:
    postfix += stack.pop()
print(postfix)
