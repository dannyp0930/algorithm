N = int(input())
arr = list(map(int, input().split()))
lst = list(map(int, input().split()))
maximum = -1000000000
minimum = 1000000000


def dfs(k, result, plus, minus, multi, divide):
    global maximum, minimum
    if k == N:
        if maximum < result:
            maximum = result
        if minimum > result:
            minimum = result
        return
    if plus:
        dfs(k + 1, result + arr[k], plus - 1, minus, multi, divide)
    if minus:
        dfs(k + 1, result - arr[k], plus, minus - 1, multi, divide)
    if multi:
        dfs(k + 1, result * arr[k], plus, minus, multi - 1, divide)
    if divide:
        if result < 0 and arr[k] > 0:
            dfs(k + 1, -(-result // arr[k]), plus, minus, multi, divide - 1)
        else:
            dfs(k + 1, result // arr[k], plus, minus, multi, divide - 1)


dfs(1, arr[0], lst[0], lst[1], lst[2], lst[3])
print(maximum)
print(minimum)
