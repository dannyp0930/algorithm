def dfs(idx, cnt):
    global ans
    if cnt == K - 5:
        read = 0
        for word in words:
            for ch in word:
                if not learn[ord(ch) - ord('a')]:
                    break
            else:
                read += 1
        ans = max(ans, read)
        return
    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = 1
            dfs(i, cnt + 1)
            learn[i] = 0


N, K = map(int, input().split())
words = [input()[4:-4] for _ in range(N)]
ans = 0
if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    learn = [0] * 26
    for ch in ['a', 'n', 't', 'i', 'c']:
        learn[ord(ch) - ord('a')] = 1
    dfs(0, 0)
    print(ans)
