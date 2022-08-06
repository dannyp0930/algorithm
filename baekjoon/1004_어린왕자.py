for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    ans = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        cond1 = (cx - x1) ** 2 + (cy - y1) ** 2 < r ** 2
        cond2 = (cx - x2) ** 2 + (cy - y2) ** 2 < r ** 2
        if cond1 ^ cond2:
            ans += 1
    print(ans)
