import sys
sys.stdin = open('1970.txt', 'r')

moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for T in range(1, int(input()) + 1):
    N = int(input())
    cnt = []
    for money in moneys:
        cnt.append(N // money)
        N = N % money
    print('#{}'.format(T))
    print(*cnt)
