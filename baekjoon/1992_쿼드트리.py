import sys


def divide(r, c, n):
    global result
    first = arr[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if arr[i][j] != first:
                result += '('
                for i in range(2):
                    for j in range(2):
                        divide(r + n // 2 * i, c + n // 2 * j, n // 2)
                result += ')'
                return
    result += str(first)
    return


input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
result = ''
divide(0, 0, N)
print(result)
