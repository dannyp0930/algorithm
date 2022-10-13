import sys
input = sys.stdin.readline
mod = 1000000007


def init(s, e, n):
    if s == e:
        tree[n] = arr[s]
        return tree[n]
    m = (s + e) // 2
    tree[n] = init(s, m, n * 2) * init(m + 1, e, n * 2 + 1) % mod
    return tree[n]


def section(s, e, n, l, r):
    if r < s or e < l:
        return 1
    if l <= s and e <= r:
        return tree[n]
    m = (s + e) // 2
    return section(s, m, n * 2, l, r) * section(m + 1, e, n * 2 + 1, l, r) % mod


def update(s, e, n, i, v):
    if i < s or i > e:
        return
    if s == e:
        tree[n] = v
        return
    m = (s + e) // 2
    update(s, m, n * 2, i, v)
    update(m + 1, e, n * 2 + 1, i, v)
    tree[n] = tree[n * 2] * tree[n * 2 + 1] % mod


N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0] * 4 * N
init(0, N - 1, 1)
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, N - 1, 1, b - 1, c)
        arr[b - 1] = c
    else:
        print(section(0, N - 1, 1, b - 1, c - 1))
