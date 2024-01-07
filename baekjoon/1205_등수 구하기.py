N, T, P = map(int, input().split())
if N:
    scores = list(map(int, input().split()))
    if N == P and scores[-1] >= T:
            print(-1)
    else:
        ans = 1
        for i, s in enumerate(scores):
            if s <= T:
                break
            ans += 1
        print(ans)
else:
    print(1)
