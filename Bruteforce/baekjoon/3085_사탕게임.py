def check():
    result = 1
    for i in range(N):

        # 행 비교
        cnt = 1
        for j in range(1, N):
            if arr[i][j] == arr[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            if result < cnt:
                result = cnt

        # 열 비교
        cnt = 1
        for k in range(1, N):
            if arr[k][i] == arr[k - 1][i]:
                cnt += 1
            else:
                cnt = 1
            if result < cnt:
                result = cnt
    return result


N = int(input())
arr = [list(input()) for _ in range(N)]
ans = 0
for r in range(N):
    for c in range(N):

        # 위 아래 바꾸기
        if r < N - 1:
            arr[r][c], arr[r + 1][c] = arr[r + 1][c], arr[r][c]
            tmp = check()

            if ans < tmp:
                ans = tmp

            arr[r][c], arr[r + 1][c] = arr[r + 1][c], arr[r][c]

        # 좌 우 바꾸기
        if c < N - 1:
            arr[r][c], arr[r][c + 1] = arr[r][c + 1], arr[r][c]
            tmp = check()

            if ans < tmp:
                ans = tmp

            arr[r][c], arr[r][c + 1] = arr[r][c + 1], arr[r][c]
print(ans)
