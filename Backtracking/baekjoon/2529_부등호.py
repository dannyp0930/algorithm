def possible(i, j, k):
    if k == '<':
        return i < j
    return i > j


def solve(cnt, num):
    global max_num, min_num
    if cnt == n + 1:
        if not min_num:
            min_num = num
        else:
            max_num = num
        return
    for i in range(10):
        if not visit[i]:
            if not cnt or possible(num[-1], str(i), sign[cnt - 1]):
                visit[i] = 1
                solve(cnt + 1, num + str(i))
                visit[i] = 0


n = int(input())
sign = input().split()
visit = [0] * 10
max_num, min_num = '', ''
solve(0, '')
print(max_num)
print(min_num)
