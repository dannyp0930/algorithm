for _ in range(int(input())):
    x, y = map(int, input().split())
    d = y - x
    n = 0
    while 1:
        if d <= n * (n + 1):
            break
        n += 1
    if n ** 2 >= d:
        print(2 * n - 1)
    else:
        print(2 * n)