import sys
input = sys.stdin.readline


def myround(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    return int(num)


n = int(input())
if n:
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    idx = myround(n * 0.15)
    print(myround(sum(arr[idx : n - idx]) / (n - 2 * idx)))
else:
    print(0)
