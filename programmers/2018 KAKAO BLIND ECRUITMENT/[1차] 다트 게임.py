def solution(dartResult):
    stack = []
    dartResult = dartResult.replace('10', 'A')
    bonus = {'S': 1, 'D': 2, 'T': 3}
    for ch in dartResult:
        if ch.isdigit() or ch == 'A':
            stack.append(10 if ch == 'A' else int(ch))
        elif ch in bonus.keys():
            num = stack.pop()
            stack.append(num ** bonus[ch])
        elif ch == '#':
            stack[-1] *= -1
        elif ch == '*':
            num = stack.pop()
            if len(stack):
                stack[-1] *= 2
            stack.append(num * 2)
    return sum(stack)
