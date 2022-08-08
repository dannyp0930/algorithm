def mul(A, B):
    tmp = [[0] * 8 for _ in range(8)]
    for r in range(8):
        for c in range(8):
            for i in range(8):
                tmp[r][c] += A[r][i] * B[i][c]
                tmp[r][c] %= mod
        tmp[r][c] %= mod
    return tmp


def pow(graph, k):
    if k == 1:
        return graph
    res = pow(graph, k // 2)
    res = mul(res, res)
    if k % 2:
        res = mul(res, graph)
    return res


mod = 1000000007
graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]
D = int(input())
ans = pow(graph, D)
print(ans[0][0])