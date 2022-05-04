def convert(num, base):
    tmp = '0123456789ABCDEF'
    q, r = divmod(num, base)

    if not q:
        return tmp[r]
    return convert(q, base) + tmp[r]


def solution(n, t, m, p):
    answer = ''
    number = ''
    for i in range(m * t):
        number += convert(i, n)
    for j in range(p - 1, len(number), m):
        answer += number[j]
        if len(answer) == t:
            break
    return answer
