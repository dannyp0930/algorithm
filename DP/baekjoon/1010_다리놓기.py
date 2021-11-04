for T in range(int(input())):
    N, M = map(int, input().split())
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if i == j:
                dp[i][j] = 1
            elif j == 1:
                dp[i][j] = i
    for i in range(3, M + 1):
        for j in range(2, N + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    print(dp[M][N])

# DFS: 조합
# def comb(idx, k):
#     global ans
#     if k == N:
#         ans += 1
#         return
#     for i in range(idx, M):
#         if not visit[i]:
#             visit[i] = 1
#             comb(i + 1, k + 1)
#             visit[i] = 0
# 
# 
# for T in range(int(input())):
#     N, M = map(int, input().split())
#     visit = [0] * (M + 1)
#     stack = []
#     ans = 0
#     comb(0, 0)
#     print(ans)
