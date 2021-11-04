import sys
sys.stdin = open('1961.txt', 'r')


def rotate(lst, n):
    new_lst = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_lst[j][n - i - 1] = lst[i][j]
    return new_lst


T = int(input())
for tc in range(1, T + 1):
    print('#{0}'.format(tc))
    N = int(input())
    arr = [input().split() for _ in range(N)]
    arr_90 = rotate(arr, N)
    arr_180 = rotate(arr_90, N)
    arr_270 = rotate(arr_180, N)
    for i in range(N):
        for j in range(N):
            print(arr_90[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(arr_180[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(arr_270[i][j], end='')
        print()
