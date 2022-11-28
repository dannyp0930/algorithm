def solution(S, T):
    while len(T) > len(S):
        if T[-1] == 'A':
            T = T[:-1]
        else:
            T = T[:-1][::-1]
        if S == T:
            return 1
    return 0


S = input()
T = input()
print(solution(S, T))