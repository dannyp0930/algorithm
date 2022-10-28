def solution(arr):

    def quad_tree(r, c, l):
        n = arr[r][c]
        for i in range(r, r + l):
            for j in range(c, c + l):
                if arr[i][j] != n:
                    l //= 2
                    quad_tree(r, c, l)
                    quad_tree(r, c + l, l)
                    quad_tree(r + l, c, l)
                    quad_tree(r + l, c + l, l)
                    return
        answer[n] += 1

    answer = [0, 0]
    l = len(arr)
    quad_tree(0, 0, l)
    return answer
