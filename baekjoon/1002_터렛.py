for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    # 원이 두 교점을 가지는 경우
    if abs(r1 - r2) < d < r1 + r2:
        print(2)
    # 원이 만나지 않는 경우
    elif d > r1 + r2:
        print(0)
    # 원이 외접하는 경우
    elif d == r1 + r2:
        print(1)
    # 원이 내접하는 경우
    elif d == abs(r1 - r2) and d:
        print(1)
    # 한 원이 다른 원에 포함되는 경우
    elif d < abs(r1 - r2):
        print(0)
    # 두 원이 일치하는 경우
    else:
        print(-1)
