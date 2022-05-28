import sys

input = sys.stdin.readline
N, r, c = map(int, input().split())
ans = 0
while N:
    N -= 1
    if r < 2 ** N and c < 2 ** N:
        pass
    elif r < 2 ** N and c >= 2 ** N:
        ans += 4 ** N
        c -= 2 ** N
    elif r >= 2 ** N and c < 2 ** N:
        ans += 4 ** N * 2
        r -= 2 ** N
    else:
        ans += 4 ** N * 3
        r -= 2 ** N     
        c -= 2 ** N
print(ans)
