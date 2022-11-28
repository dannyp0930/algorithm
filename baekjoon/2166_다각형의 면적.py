N = int(input())
x, y = [], []
S = 0
for _ in range(N):
    p = list(map(int, input().split()))
    x.append(p[0])
    y.append(p[1])
x, y = x + [x[0]], y + [y[0]]
for i in range(N):
    S += x[i] * y[i + 1] - x[i + 1] * y[i]
print(round(abs(S) / 2, 1))
