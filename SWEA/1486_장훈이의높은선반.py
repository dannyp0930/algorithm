import sys
sys.stdin = open('1486.txt', 'r')


def subset(k):
    global lst, ans
    if k == N:
        if sum(lst) < B:
            return
        if ans > sum(lst):
            ans = sum(lst)
            return
    else:
        lst.append(S[k])
        subset(k + 1)
        lst.pop()
        subset(k + 1)


for T in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))
    lst = []
    ans = sum(S)
    subset(0)
    print('#{} {}'.format(T, ans - B))
