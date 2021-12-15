def solution(n):
    ternary = ''
    while n:
        ternary += str(n % 3)
        n = n // 3
    return int(ternary, 3)
