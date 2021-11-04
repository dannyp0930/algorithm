# 백트래킹


# 행, 열, 개수, 색
def dfs(x, y, cnt, color):
    # 열 값이 범위를 벗어나는 경우
    if y >= N:
        # 다음 행으로 이동
        x += 1
        # 열 순서 변경
        y = 0 if y % 2 else 1
    # 탐색을 마치면
    if x == N:
        # 최댓값 비교
        ans[color] = max(ans[color], cnt)
        return
    # 비숍을 놓을 수 있는 경우
    if arr[x][y] and not left[x + y] and not right[x - y + N - 1]:
        left[x + y] = right[x - y + N - 1] = 1
        dfs(x, y + 2, cnt + 1, color)
        left[x + y] = right[x - y + N - 1] = 0
    # 비숍을 놓지 않고 다음으로 넘어가는 경우
    dfs(x, y + 2, cnt, color)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 왼쪽 대각선
left = [0] * (2 * N - 1)
# 오른쪽 대각선
right = [0] * (2 * N - 1)
# 0: 흑, 1: 백
ans = [0, 0]
dfs(0, 0, 0, 0)
dfs(0, 1, 0, 1)
print(sum(ans))
