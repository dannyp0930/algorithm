def mul(A, B):
    C = [[0] * 2 for _ in range(2)]
    for r in range(2):
        for c in range(2):
            tmp = 0
            for i in range(2):
                tmp += A[r][i] * B[i][c]
            C[r][c] = tmp % p
    return C


def power(A, n):
    if n == 1:
        for r in range(2):
            for c in range(2):
                A[r][c] %= p
        return A
    tmp = power(A, n // 2)
    if not n % 2:
        return mul(tmp, tmp)
    else:
        return mul(mul(tmp, tmp), A)


n = int(input())
p = 1000000007
A = [[1, 1], [1, 0]]
print(power(A, n)[0][1])
