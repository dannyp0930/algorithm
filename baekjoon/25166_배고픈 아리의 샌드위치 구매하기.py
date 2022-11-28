def solution(S, M):
    if S < 1024:
        return 'No thanks'
    S -= 1023
    for _ in range(10):
        if S & 1 != M & 1:
            return 'Impossible'
        S >>= 1
        M >>= 1
    return 'Thanks'


S, M = map(int, input().split())
print(solution(S, M))
