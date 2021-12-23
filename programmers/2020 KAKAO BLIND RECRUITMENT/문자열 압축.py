def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        com = ''
        tmp = s[:i]
        cnt = 1
        for j in range(i, len(s), i):
            if tmp == s[j:j + i]:
                cnt += 1
            else:
                if cnt > 1:
                    com += str(cnt)
                com += tmp
                tmp = s[j:j + i]
                cnt = 1
        if cnt > 1:
            com += str(cnt)
        com += tmp
        answer = min(answer, len(com))
    return answer
