import sys
sys.stdin = open('6485.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bus_stop = [0] * 5001
    for _ in range(N):
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            bus_stop[i] += 1
    P = int(input())
    print('#{0}'.format(tc), end='')
    for _ in range(P):
        c = int(input())
        print(' {0}'.format(bus_stop[c]), end='')
    print()
