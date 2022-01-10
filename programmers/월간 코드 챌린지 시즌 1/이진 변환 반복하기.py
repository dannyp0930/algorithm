def solution(s):
    times = 0
    zeros = 0
    while s != '1':
        tmp = ''
        for ch in s:
            if ch == '1':
                tmp += ch
            else:
                zeros += 1
        s = bin(len(tmp))[2:]
        times += 1
    return [times, zeros]
