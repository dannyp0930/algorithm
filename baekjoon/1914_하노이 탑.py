def hanoi(n, s, m, e):
    if n == 0:
        return
    hanoi(n - 1, s, e, m)
    print(s, e)
    hanoi(n - 1, m, s, e)


N = int(input())
print(2 ** N - 1)
if N <= 20:
    hanoi(N, 1, 2, 3)
