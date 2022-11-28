import sys

input = sys.stdin.readline

def check_color(r, c, n):
    first = arr[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if arr[i][j] != first:
                return False
    if first:
        return 'blue'
    return 'white'

def divide(r, c, n):
    global white, blue
    check = check_color(r, c, n)
    if check:
        if check == 'white':
            white += 1
        else:
            blue += 1
        return
    n //= 2
    divide(r, c, n)
    divide(r + n, c, n)
    divide(r, c + n, n)
    divide(r + n, c + n, n)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
white = blue = 0
divide(0, 0, N)
print(white)
print(blue)