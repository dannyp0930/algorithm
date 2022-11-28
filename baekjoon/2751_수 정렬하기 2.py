N = int(input())
lst = [int(input()) for _ in range(N)]


# 병합정렬
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merge = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merge.append(left[l])
            l += 1
        else:
            merge.append(right[r])
            r += 1
    merge += left[l:]
    merge += right[r:]
    return merge


result = merge_sort(lst)
for num in result:
    print(num)
