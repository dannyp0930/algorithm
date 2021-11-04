N = int(input())        # 정수 N
memo = [0, 0, 1, 1]     # N이 1, 2, 3일 때 미리 계산
for i in range(4, N + 1):
    memo.append(memo[i - 1] + 1)    # -1을 먼저 수행
    if not i % 3 and memo[i] > memo[i // 3] + 1:    # 3으로 나누어 떨어지는 경우
        memo[i] = memo[i // 3] + 1
    if not i % 2 and memo[i] > memo[i // 2] + 1:    # 2로 나누어 떨어지는 경우
        memo[i] = memo[i // 2] + 1
print(memo[N])
