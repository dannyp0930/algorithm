N = int(input())
arr = list(map(int, input().split()))
s, e = 0, N - 1
max_sol = 2000000000
ans_s, ans_e = s, e
while s < e:
    sol = arr[s] + arr[e]
    if max_sol > abs(sol):
        max_sol = abs(sol)
        ans_s, ans_e = s, e
    if sol < 0:
        s += 1
    else:
        e -= 1
print(arr[ans_s], arr[ans_e])
