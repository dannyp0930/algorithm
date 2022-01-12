def solution(n, words):
    times = [0] * n
    stack = []
    i = 0
    flag = False
    while words:
        times[i] += 1
        temp = words.pop(0)
        if stack:
            if stack[-1][-1] != temp[0] or temp in stack:
                flag = True
                break
        stack.append(temp)
        i += 1
        if i == n:
            i = 0
    if flag:
        return [i + 1, times[i]]
    return [0, 0]
