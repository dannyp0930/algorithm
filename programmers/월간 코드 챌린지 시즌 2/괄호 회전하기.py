def determine(s):
    stack = []
    for ch in s:
        if ch == '[' or ch == '{' or ch == '(':
            stack.append(ch)
        elif (stack and ch ==']' and stack[-1] == '[') or (stack and ch == '}' and stack[-1] == '{') or (stack and ch == ')' and stack[-1] == '('):
            stack.pop()
        else:
            return False
    if stack:
        return False
    return True

def solution(s):
    answer = 0
    for i in range(len(s)):
        ns = s[i:] + s[:i]
        if determine(ns):
            answer += 1
    return answer