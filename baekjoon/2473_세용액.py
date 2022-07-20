N = int(input())
arr = list(map(int, input().split()))
arr.sort()
max_sol = 3000000001
res = (0, 0, 0)
flag = False
for i in range(N - 2):
    s, e = i + 1, N - 1
    while s < e:
        sol = arr[i] + arr[s] + arr[e]
        if max_sol > abs(sol):
            max_sol = abs(sol)
            res = (i, s, e)
        if sol < 0:
            s += 1
        elif sol > 0:
            e -= 1
        else:
            flag = True
            break
    if flag:
        break
print(arr[res[0]], arr[res[1]], arr[res[2]])
