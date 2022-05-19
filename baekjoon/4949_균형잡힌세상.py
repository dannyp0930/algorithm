def find(string):
    for ch in string:
        if ch == '[' or ch == '(':
            stack.append(ch)
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return 'no'
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 'no'
    if stack:
        return 'no'
    return 'yes'

while 1:
    string = input()
    if string == '.':
        break
    stack = []
    print(find(string))
