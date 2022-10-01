def reverse(r, c):
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            A[i][j] = int(not A[i][j])


def solution():
    if N < 3 or M < 3:
        if A == B:
            return 0
        return -1
    cnt = 0
    for i in range(N - 2):
        for j in range(M - 2):
            if A[i][j] != B[i][j]:
                cnt += 1
                reverse(i, j)
    if A != B:
        return -1
    return cnt
    

N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]
print(solution())