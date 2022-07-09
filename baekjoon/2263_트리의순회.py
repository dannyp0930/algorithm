import sys
sys.setrecursionlimit(10**6)


def pre_order(i_s, i_e, p_s, p_e):
    if i_s > i_e or p_s > p_e:
        return
    root = post_order[p_e]
    pos = index[root]
    size = pos - i_s
    print(root, end=' ')
    pre_order(i_s, pos - 1, p_s, p_s + size - 1)
    pre_order(pos + 1, i_e, p_s + size, p_e - 1)


n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
index = [0] * (n + 1)
for i in range(n):
    index[in_order[i]] = i
pre_order(0, n - 1, 0, n - 1)
