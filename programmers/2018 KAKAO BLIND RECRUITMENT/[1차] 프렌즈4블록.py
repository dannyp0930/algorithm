def solution(m, n, board):
    answer = 0
    arr = []
    for lst in board:
        arr.append([ch for ch in lst])

    while True:
        checked = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if arr[i][j] == 0: continue
                if arr[i][j] == arr[i][j + 1] == arr[i + 1][j] == arr[i + 1][j + 1]:
                    checked.add((i, j))
                    checked.add((i, j + 1))
                    checked.add((i + 1, j))
                    checked.add((i + 1, j + 1))
        if not checked:
            return answer
        answer += len(checked)

        # 블록 삭제
        for x, y in checked:
            arr[x][y] = 0

        # 삭제된 블록 위에서 부터 시작
        for r, c in list(checked):
            now = r - 1
            down = r
            while now >= 0:
                # 아래가 비어있고 현재 위치가 차있다면
                if not arr[down][c] and arr[now][c]:
                    # 아래로 이동
                    arr[down][c] = arr[now][c]
                    arr[now][c] = 0
                    down -= 1
                now -= 1
