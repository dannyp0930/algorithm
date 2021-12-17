def solution(arr1, arr2):
    answer = []
    n = len(arr1)
    m = len(arr1[0])
    for r in range(n):
        tmp = []
        for c in range(m):
            tmp.append(arr1[r][c] + arr2[r][c])
        answer.append(tmp)
    return answer
