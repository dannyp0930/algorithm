import sys
input = sys.stdin.readline
MAX_VALUE = 10 ** 9


def init(s, e, node):
    if s == e:
        tree[node] = (arr[s], arr[s])
        return tree[node]
    m = (s + e) // 2
    left = init(s, m, node * 2)
    right = init(m + 1, e, node * 2 + 1)
    tree[node] = (min(left[0], right[0]), max(left[1], right[1]))
    return tree[node]


def find(s, e, node, l, r):
    if r < s or e < l:
        return (MAX_VALUE, 0)
    if l <= s and e <= r:
        return tree[node]
    m = (s + e) // 2
    left = find(s, m, node * 2, l, r)
    right = find(m + 1, e, node * 2 + 1, l, r)
    return (min(left[0], right[0]), max(left[1], right[1]))


N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0] * 4 * N
init(0, N - 1, 1)
for _ in range(M):
    a, b = map(int, input().split())
    res = find(0, N - 1, 1, a - 1, b - 1)
    print(res[0], res[1])
