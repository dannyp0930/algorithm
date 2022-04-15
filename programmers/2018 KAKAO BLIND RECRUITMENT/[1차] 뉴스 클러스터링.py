def solution(str1, str2):
    n1 = len(str1)
    n2 = len(str2)

    # 중복 집합
    arr1, arr2 = [], []

    for i in range(0, n1 - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            arr1.append(str1[i:i + 2].lower())

    for i in range(0, n2 - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            arr2.append(str2[i:i + 2].lower())

    # 기존 중복집합의 크기
    n_arr1, n_arr2 = len(arr1), len(arr2)

    # 교집합 구하기
    intersection = []
    for val in arr2:
        if val in arr1:
            arr1.remove(val)
            intersection.append(val)

    # 교집합의 크기
    n_inter = len(intersection)

    # 합집합의 크기
    n_union = n_arr1 + n_arr2 - n_inter

    if not n_inter and not n_union:
        return 65536
    else:
        return int(n_inter / n_union * 65536)
