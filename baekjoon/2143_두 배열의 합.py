def lower_bound(arr, t, s, e):
    while s < e:
        m = (s + e) // 2
        if arr[m] < t:
            s = m + 1
        else:
            e = m
    return s


def upper_bound(arr, t, s, e):
    while s < e:
        m = (s + e) // 2
        if arr[m] <= t:
            s = m + 1
        else:
            e = m
    return s

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
A_list = []
for i in range(n):
    s = 0
    for j in range(i, n):
        s += A[j]
        A_list.append(s)
B_list = []
for i in range(m):
    s = 0
    for j in range(i, m):
        s += B[j]
        B_list.append(s)
ans = 0
B_list.sort()
for a in A_list:
    t = T - a
    s, e = 0, len(B_list)
    l = lower_bound(B_list, t, s, e)
    u = upper_bound(B_list, t, s, e)
    ans += u - l
print(ans)
