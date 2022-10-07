import sys
input = sys.stdin.readline


def init(s, e, n):
    if s == e:
        tree[n] = arr[s]
        return tree[n]
    m = (s + e) // 2
    tree[n] = init(s, m, n * 2) + init(m + 1, e, n * 2 + 1)
    return tree[n]


def prefix_sum(s, e, n, l, r):
    if r < s or e < l: return 0
    if l <= s and e <= r: return tree[n]
    m = (s + e) // 2
    return prefix_sum(s, m, n * 2, l, r) + prefix_sum(m + 1, e, n * 2 + 1, l, r)


def update(s, e, n, i, v):
    if i < s or i > e: return
    tree[n] += v
    if s == e: return
    m = (s + e) // 2
    update(s, m, n * 2, i, v)
    update(m + 1, e, n * 2 + 1, i, v)


N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0] * 4 * N
init(0, N - 1, 1)
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, N - 1, 1, b - 1, c - arr[b - 1])
        arr[b - 1] = c
    else:
        print(prefix_sum(0, N - 1, 1, b - 1, c - 1))