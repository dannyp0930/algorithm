from collections import Counter


N = int(input())
arr = list(map(int, input().split()))
arr_cnt = Counter(arr)
ans = [-1] * N
stack = []
for i in range(N):
    while stack and arr_cnt[arr[stack[-1]]] < arr_cnt[arr[i]]:
        ans[stack.pop()] = arr[i]
    stack.append(i)
print(*ans)
