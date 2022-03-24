def kain(m, n, x, y):
    while x < M * N:
        if not (x - y) % n:
            return x
        x += m
    return -1


for _ in range(int(input())):
    M, N, X, Y = map(int, input().split())
    print(kain(M, N, X, Y))
