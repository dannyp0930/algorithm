import sys
sys.stdin = open('3308.txt', 'r')

for T in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    LIS = [0] * N
    ans = 0
    for num in arr:
        i, j = 0, ans
        while i != j:
            m = (i + j) // 2
            if LIS[m] < num:
                i = m + 1
            else:
                j = m
        LIS[i] = num
        if ans < i + 1:
            ans = i + 1
    print('#{} {}'.format(T, ans))
