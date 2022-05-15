# 색종이 붙일 수 있는지 체크
def check(i, j, length):
    for m in range(i, i + length + 1):
        for n in range(j, j + length + 1):
            if not arr[m][n]:
                return False
    return True


def dfs(r, c, cnt):
    global ans, papers
    # 마지막 행까지 다 돌면 개수 판별
    if r == 10:
        ans = min(ans, cnt)
        return

    # 마지막 열에 도달하면 다음 행으로
    if c == 10:
        dfs(r + 1, 0, cnt)
        return

    # 색종이를 붙여야 하면
    if arr[r][c]:
        for k in range(5):

            # 이 크기의 색종이를 다 붙였다면
            if papers[k] == 5: continue

            # 색종이가 경계를 넘어가면
            if r + k >= 10 or c + k >= 10: continue

            # 색종이 붙일 수 있는지 체크
            if check(r, c, k):
                # 색종이를 붙이고
                for i in range(r, r + k + 1):
                    for j in range(c, c + k + 1):
                        arr[i][j] = 0
                # 사용 개수 증가
                papers[k] += 1
                # 다음으로 넘어가기
                dfs(r, c + k + 1, cnt + 1)
                # 원래대로 돌리기
                for i in range(r, r + k + 1):
                    for j in range(c, c + k + 1):
                        arr[i][j] = 1
                # 사용 개수 감소
                papers[k] -= 1
    else:
        dfs(r, c + 1, cnt)


arr = [list(map(int, input().split())) for _ in range(10)]
papers = [0, 0, 0, 0, 0]
ans = 26
dfs(0, 0, 0)
if ans == 26:
    ans = -1
print(ans)
