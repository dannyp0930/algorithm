import sys


input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    candi = [list(map(int, input().split())) for _ in range(N)]
    candi.sort()
    t = 0
    res = 1
    for i in range(1, N):
        if candi[i][1] < candi[t][1]:
            t = i
            res += 1
    print(res)
