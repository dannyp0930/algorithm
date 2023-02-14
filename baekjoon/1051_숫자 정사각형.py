def is_square(r, c, l):
    if arr[r][c] == arr[r + l - 1][c] == arr[r][c + l - 1] == arr[r + l - 1][c + l - 1]:
        return True
    return False


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
L = N if N < M else M
ans = 1
for r in range(N):
    for c in range(M):
        for l in range(1, L + 1):
            if r + l - 1 >= N or c + l - 1 >= M:
                continue
            if is_square(r, c, l):
                ans = l if ans < l else ans
print(ans ** 2)
