def binary(t):
    s, e = 0, N - 1
    while s <= e:
        m = (s + e) // 2
        if cards[m] == t:
            return 1
        if cards[m] < t:
            s = m + 1
        else:
            e = m - 1
    return 0

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
check = list(map(int, input().split()))
for num in check:
    print(binary(num), end=' ')