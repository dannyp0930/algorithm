N = int(input())
stars = [[' '] * (4 * N - 3) for _ in range(4 * N - 3)]


def fill(n, r, c):
    if n == 1:
        stars[r][c] = '*'
        return
    l = 4 * n - 3
    for i in range(l):
        stars[r][c + i] = '*'
        stars[r + i][c] = '*'
        stars[r + l - 1][c + i] = '*'
        stars[r + i][c + l - 1] = '*'
    fill(n - 1, r + 2, c + 2)


fill(N, 0, 0)
for star in stars:
    print(''.join(star))
