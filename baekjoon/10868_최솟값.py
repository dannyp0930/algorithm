import sys
input = sys.stdin.readline
MAX_VALUE = int(1e9)


def init(s, e, node):
    if s == e:
        tree[node] = arr[s]
        return tree[node]
    m = (s + e) // 2
    tree[node] = min(init(s, m, node * 2), init(m + 1, e, node * 2 + 1))
    return tree[node]


def find(s, e, node, l, r):
    if r < s or e < l:
        return MAX_VALUE
    if l <= s and e <= r:
        return tree[node]
    m = (s + e) // 2
    return min(find(s, m, node * 2, l, r), find(m + 1, e, node * 2 + 1, l, r))


N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0] * 4 * N
init(0, N - 1, 1)
for _ in range(M):
    a, b = map(int, input().split())
    print(find(0, N - 1, 1, a - 1, b - 1))
