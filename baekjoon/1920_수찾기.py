def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == target:
            return 1
        elif A[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
arr = list(map(int, input().split()))
for num in arr:
    print(binary_search(0, N - 1, num))
