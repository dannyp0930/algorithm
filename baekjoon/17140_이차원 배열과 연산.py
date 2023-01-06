from collections import Counter
from functools import reduce


def calc(arr):
    max_length = 0
    for i in range(len(arr)):
        counter = Counter(arr[i])
        del counter[0]
        counter = list(counter.items())
        counter.sort(key=lambda x: (x[1], x[0]))
        if len(counter) > 50:
            counter = counter[:50]
        arr[i] = reduce(lambda x, y: list(x) + list(y),
                        counter[1:], list(counter[0]))
        max_length = max(max_length, len(arr[i]))
    for i in range(len(arr)):
        if len(arr[i]) < max_length:
            arr[i].extend([0] * (max_length - len(arr[i])))


r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
ans = 0
while 1:
    if r - 1 < len(arr) and c - 1 < len(arr[0]) and arr[r - 1][c - 1] == k:
        print(ans)
        break
    if len(arr) >= len(arr[0]):
        calc(arr)
    else:
        arr = list(map(list, zip(*arr)))
        calc(arr)
        arr = list(map(list, zip(*arr)))
    ans += 1
    if ans > 100:
        print(-1)
        break
