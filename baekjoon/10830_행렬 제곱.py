import sys

def mult(A, B):
    res = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            tmp = 0
            for i in range(N):
                tmp += A[r][i] * B[i][c]
            res[r][c] = tmp % 1000
    return res

def pow(A, n):
    if n == 1:
        for r in range(N):
            for c in range(N):
                A[r][c] %= 1000
        return A
    else:
        if n % 2 == 0:
            x = pow(A, n // 2)
            return mult(x, x)
        else:
            x = pow(A, n - 1)
            return mult(x, A)

input = sys.stdin.readline
N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = pow(arr, B)
for lst in result:
    print(*lst)
