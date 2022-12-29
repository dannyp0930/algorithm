def calc(a, op, b):
    a, b = int(a), int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b


def dfs(idx, value):
    global res
    if idx == N - 1:
        res = max(res, value)
        return
    # 묶은 경우
    if idx + 2 < N:
        tmp = calc(value, exp[idx + 1], exp[idx + 2])
        dfs(idx + 2, tmp)
    # 묶지 않은 경우
    if idx + 4 < N:
        tmp = calc(value, exp[idx + 1], calc(*exp[idx + 2: idx + 5]))
        dfs(idx + 4, tmp)


res = -1 * 2 ** 31
N = int(input())
exp = input()
dfs(0, int(exp[0]))
print(res)
