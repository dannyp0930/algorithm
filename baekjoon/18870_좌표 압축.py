import sys

input = sys.stdin.readline
N = int(input())
X = list(map(int, input().split()))
order = sorted(list(set(X)))
X_dic = { order[i]: i for i in range(len(order))}
compress = [ X_dic[X[i]] for i in range(N)]
print(*compress)