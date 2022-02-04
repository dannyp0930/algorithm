def solution(n):
    arr = [[0] * i for i in range(1, n + 1)]
    r, c = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                r += 1
            elif i % 3 == 1:
                c += 1
            else:
                r -= 1
                c -= 1
            arr[r][c] = num
            num += 1
    return sum(arr, [])
