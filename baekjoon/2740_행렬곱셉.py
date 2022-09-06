N, M = map(int, input().split())                                   
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]
C = [[0] * K for _ in range(N)]
for n in range(N):
    for m in range(M):
        for k in range(K):
            C[n][k] += A[n][m] * B[m][k]
for r in range(N):
    print(*C[r])
