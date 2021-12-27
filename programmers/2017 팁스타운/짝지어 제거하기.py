def solution(s):
    stack = []
    for ch in s:
        if not stack:
            stack.append(ch)
        else:
            if stack[-1] == ch:
                stack.pop()
                continue
            stack.append(ch)
    if stack:
        return 0
    return 1
