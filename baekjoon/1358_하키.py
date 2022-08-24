def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def boundary(x, y):
    if X <= x <= X + W and Y <= y <= Y + H: return True
    if distance(x, y, X, Y + H // 2) <= H // 2: return True
    if distance(x, y, X + W, Y + H // 2) <= H // 2: return True
    return False


W, H, X, Y, P = map(int, input().split())
cnt = 0
for _ in range(P):
    x, y = map(int, input().split())
    if boundary(x, y):
        cnt += 1
print(cnt)
