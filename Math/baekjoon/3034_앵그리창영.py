N, W, H = map(int, input().split())
# 대각선
D = (W ** 2 + H ** 2 ) ** 0.5
for _ in range(N):
    length = int(input())
    if length > D:
        print('NE')
    else:
        print('DA')
