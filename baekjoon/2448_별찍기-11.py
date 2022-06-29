import sys


def draw(n, r, c):
    if n == 1:
        for i in range(3):
            for j in range(5):
                arr[r + i][c + j] = stars[i][j]
        return
    draw(n // 2, r, c + 3 * n // 2)
    draw(n // 2, r + 3 * n // 2, c)
    draw(n // 2, r + 3 * n // 2, c + 3 * n)


stars = [
    '  *  ',
    ' * * ',
    '*****'
]
input = sys.stdin.readline
N = int(input())
arr = [[' '] * 2 * N for _ in range(N)]
draw(N // 3, 0, 0)
for lst in arr:
    print(''.join(lst))