def solution(n):
    answer = ''
    collect = ['1', '2', '4']
    while n:
        n -= 1
        answer += collect[n % 3]
        n //= 3
    return answer[::-1]
