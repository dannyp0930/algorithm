def dfs_recursion(numbers, target):
    answer = 0
    n = len(numbers)

    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        dfs(idx + 1, result + numbers[idx])
        dfs(idx + 1, result - numbers[idx])
    dfs(0, 0)
    return answer


def bfs(numbers, target):
    answer = 0
    n = len(numbers)
    Q = [(numbers[0], 0), (-1 * numbers[0], 0)]
    while Q:
        tmp, idx = Q.pop()
        idx += 1
        if idx < n:
            Q.append((tmp + numbers[idx], idx))
            Q.append((tmp - numbers[idx], idx))
        else:
            if tmp == target:
                answer += 1
    return answer
