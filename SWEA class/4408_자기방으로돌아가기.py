import sys
sys.stdin = open('4408.txt', 'r')


def div(num):
    return (int(num) + 1) // 2


def my_max(arr):
    result = 0
    for n in range(len(arr)):
        if result < arr[n]:
            result = arr[n]
    return result


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    corridor = [0] * 201
    for _ in range(N):
        a, b = map(div, input().split())
        if a < b:
            for i in range(a, b + 1):
                corridor[i] += 1
        else:
            for i in range(a, b - 1, -1):
                corridor[i] += 1

    print('#{0} {1}'.format(tc, my_max(corridor)))
