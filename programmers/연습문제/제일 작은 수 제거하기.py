def solution(arr):
    min_num = arr[0]
    for num in arr:
        if min_num > num:
            min_num = num
    arr.remove(min_num)
    if not arr:
        arr = [-1]
    return arr
