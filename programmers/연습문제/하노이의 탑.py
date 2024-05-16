def solution(n):
    ans = []

    def hanoi(N, start, via, end):
        if N == 1:
            ans.append([start, end])
        else:
            hanoi(N - 1, start, end, via)
            ans.append([start, end])
            hanoi(N - 1, via, start, end)

    hanoi(n, 1, 2, 3)
    return ans
