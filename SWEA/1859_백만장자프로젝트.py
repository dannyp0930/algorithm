import sys
sys.stdin = open('1859.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    max_price = arr[-1]
    for i in range(N - 1, -1, -1):
        if max_price > arr[i]:
            result += (max_price - arr[i])
        else:
            max_price = arr[i]
    print('#{0} {1}'.format(tc, result))
