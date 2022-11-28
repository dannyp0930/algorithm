def cnt_n(N, n):
    cnt = 0
    while N:
        cnt += N // n
        N //= n
    return cnt


n, m = map(int, input().split())
cnt_2 = cnt_n(n, 2) - cnt_n(n - m, 2) - cnt_n(m, 2)
cnt_5 = cnt_n(n, 5) - cnt_n(n - m, 5) - cnt_n(m, 5)
print(min(cnt_2, cnt_5))
