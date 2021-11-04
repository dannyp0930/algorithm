import sys
sys.stdin = open('5356.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    arr = [input() for _ in range(5)]
    result = ''
    for j in range(15):
        i = 0
        while i < 5:
            try:
                result += arr[i][j]
            except IndexError:
                pass
            i += 1
    print('#{0} {1}'.format(tc, result))
