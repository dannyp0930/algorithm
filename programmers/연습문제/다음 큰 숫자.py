def solution(n):
    N = n + 1
    cnt = bin(n).count('1')
    while 1:
        if bin(N).count('1') == cnt:
            return N
        N += 1
