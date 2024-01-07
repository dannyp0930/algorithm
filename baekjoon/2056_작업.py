import sys
input = sys.stdin.readline


N = int(input())
times = [0] * (N + 1)
for n in range(1, N + 1):
    arr = list(map(int, input().split()))
    times[n] = arr[0] + max([times[v] for v in arr[2:]]) if arr[1] else arr[0]
print(max(times))