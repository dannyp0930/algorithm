for _ in range(int(input())):
    ps = input()
    stack = []
    for s in ps:
        if not stack:
            stack.append(s)
        else:
            if stack[-1] == '(' and s == ')':
                stack.pop()
            else:
                stack.append(s)
    if stack:
        print('NO')
    else:
        print('YES')
