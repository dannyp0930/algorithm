def solution(rows, columns, queries):
    answer = []
    arr = [[i + 1 + j * columns for i in range(columns)] for j in range(rows)]
    for query in queries:
        r1, c1, r2, c2 = query
        tmp = arr[r1 - 1][c1 - 1]
        small = tmp

        for i in range(r1, r2):
            arr[i - 1][c1 - 1] = arr[i][c1 - 1]
            small = min(small, arr[i][c1 - 1])

        for i in range(c1, c2):
            arr[r2 - 1][i - 1] = arr[r2 - 1][i]
            small = min(small, arr[r2 - 1][i])

        for i in range(r2 - 2, r1 - 2, -1):
            arr[i + 1][c2 - 1] = arr[i][c2 - 1]
            small = min(small, arr[i][c2 - 1])

        for i in range(c2 - 2, c1 - 2, -1):
            arr[r1 - 1][i + 1] = arr[r1 - 1][i]
            small = min(small, arr[r1 - 1][i])

        arr[r1 - 1][c1] = tmp

        answer.append(small)
    return answer
