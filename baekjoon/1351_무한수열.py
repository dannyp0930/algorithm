def dfs(n):
    if n in arr:
        return arr[n]
    arr[n] = dfs(n // P) + dfs(n // Q)
    return arr[n]

N, P, Q = map(int, input().split())
arr = {}
arr[0] = 1
print(dfs(N))
