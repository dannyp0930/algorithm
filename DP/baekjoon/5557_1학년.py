N = int(input())
arr = list(map(int, input().split()))
dp = [[0] * 21 for _ in range(N - 1)]   # dp[i][j] : i번 연산 했을 때 j 값인 경우의 수
dp[0][arr[0]] = 1
for i in range(1, N - 1):
    for j in range(21):
        if dp[i - 1][j]:    # 만약 이전 연산에서 값이 존재한다면
            pv = j          # 이전 값 저장
            nv = arr[i]     # 연산해 줄 값 저장
            if pv - nv >= 0:    # 뺀값이 0보다 크면
                dp[i][pv - nv] += dp[i - 1][pv]
            if pv + nv <= 20:   # 더한 값이 20보다 작으면
                dp[i][pv + nv] += dp[i - 1][pv]
print(dp[N - 2][arr[N - 1]])
