import sys
sys.stdin = open('1979.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        row = col = 0
        for j in range(N):
            if arr[i][j]:
                row += 1
                if row == K:
                    if j + 1 == N or arr[i][j + 1] == 0:
                        result += 1
            else:
                row = 0
            if arr[j][i]:
                col += 1
                if col == K:
                    if j + 1 == N or arr[j + 1][i] == 0:
                        result += 1
                        col = 0
            else:
                col = 0
    print('#{0} {1}'.format(tc, result))
