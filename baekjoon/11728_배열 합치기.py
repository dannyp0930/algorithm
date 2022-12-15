N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = []
a = b = 0
while a < N or b < M:
    if a == N:
        ans.append(B[b])
        b += 1
    elif b == M:
        ans.append(A[a])
        a += 1
    elif A[a] < B[b]:
        ans.append(A[a])
        a += 1
    else:
        ans.append(B[b])
        b += 1
print(*ans)
