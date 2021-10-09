N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)
for i in range(N - 1, -1, -1):  # 마지막 날부터 역순으로 계산
    if i + arr[i][0] > N:   # 상담이 마지막 날보다 늦게 끝나면
        dp[i] = dp[i + 1]   # 전날 상담 금액
    else:
        if dp[i + 1] > arr[i][1] + dp[i + arr[i][0]]:   # 전날 상담 금액이 오늘 상담한것 보다 크다면
            dp[i] = dp[i + 1]
        else:
            dp[i] = arr[i][1] + dp[i + arr[i][0]]
print(dp[0])
