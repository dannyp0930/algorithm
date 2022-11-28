N, L = map(int, input().split())
res = 0
for i in range(L, 101):
    x = N - i * (i - 1) / 2
    if x % i == 0:
        x = int(x / i)
        if x >= 0:
            for j in range(x, x + i):
                print(j, end=' ')
            print()
            break
else:
    print(-1)
