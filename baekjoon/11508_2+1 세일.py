import sys
input = sys.stdin.readline


N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
s, e = 0, 2
ans = 0
while 1:
    if e >= N:
        ans += sum(arr[s:])
        break
    ans += sum(arr[s:e + 1]) - min(arr[s:e + 1])
    s += 3
    e += 3
print(ans)
