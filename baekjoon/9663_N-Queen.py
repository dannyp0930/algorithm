def possible(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def queen(x):
    global ans

    if x == N:
        ans += 1
        return

    for i in range(N):
        row[x] = i
        if possible(x):
            queen(x + 1)


N = int(input())
ans = 0
row = [0] * N
queen(0)
print(ans)
