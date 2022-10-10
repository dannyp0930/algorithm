def determine(arr):
    visit = [False] * N
    for i in range(1, N):
        if arr[i] == arr[i - 1]:
            continue
        # 차이 1 이상이면
        if abs(arr[i] - arr[i - 1]) > 1:
            return False
        # 이전이 더 높은 경우
        if arr[i] < arr[i - 1]:
            for j in range(i, i + L):
                if j >= N:
                    return False
                if visit[j]:
                    return False
                if arr[i] != arr[j]:
                    return False
                visit[j] = True
        # 다음이 더 높은 경우
        else:
            for j in range(i - 1, i - L - 1, -1):
                if j < 0:
                    return False
                if visit[j]:
                    return False
                if arr[i - 1] != arr[j]:
                    return False
                visit[j] = True
    return True


N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for r in range(N):
    if determine(arr[r]):
        ans += 1
for c in range(N):
    if determine([arr[r][c] for r in range(N)]):
        ans += 1
print(ans)
