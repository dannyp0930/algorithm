for _ in range(int(input())):
    command = input()
    stack1 = []
    stack2 = []
    for c in command:
        if c == '<':
            if stack1:
                stack2.append(stack1.pop())
        elif c == '>':
            if stack2:
                stack1.append(stack2.pop())
        elif c == '-':
            if stack1:
                stack1.pop()
        else:
            stack1.append(c)
    print(''.join(stack1) + ''.join(stack2[::-1]))
