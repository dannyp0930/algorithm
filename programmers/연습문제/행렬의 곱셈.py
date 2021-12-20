def solution(arr1, arr2):
    M = len(arr1)
    N = len(arr2)
    P = len(arr2[0])
    answer = [[0] * P for _ in range(M)]
    for i in range(M):
        for j in range(P):
            for k in range(N):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer
