A, B = input().split()
N, M = len(A), len(B)
ans = N
for i in range(M - N + 1):
    tmp = 0
    for j in range(N):
        if A[j] != B[i + j]:
            tmp += 1
    ans = min(ans, tmp)
print(ans)
