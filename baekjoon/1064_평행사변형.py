xa, ya, xb, yb, xc, yc = map(int, input().split())
# 기울기가 같은 경우
if (ya - yb) * (xc - xa) == (yc - ya) * (xa - xb):
    print(-1.0)
else:
    # 세 점이 이루는 삼각형 변의 길이
    length = [
        ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5,
        ((xb - xc) ** 2 + (yb - yc) ** 2) ** 0.5,
        ((xa - xc) ** 2 + (ya - yc) ** 2) ** 0.5
    ]
    print((max(length) - min(length)) * 2)