# 문자열 나누기
def separate(s):
    cnt1 = cnt2 = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt1 == cnt2:
            return s[:i + 1], s[i + 1:]


# 올바른 문자열 확인
def determine(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()
    return True


def solution(p):
    # 1
    if not p:
        return p
    # 2
    u, v = separate(p)

    # 3
    if determine(u):
        return u + solution(v)

    # 4
    answer = '(' + solution(v) + ')'
    u = u[1:-1]
    for ch in u:
        if ch == '(':
            answer += ')'
        else:
            answer += '('
    return answer
