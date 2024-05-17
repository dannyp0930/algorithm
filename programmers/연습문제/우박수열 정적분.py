def solution(k, ranges):
    ans = []

    def lothar(k):
        arr = [k]
        while k > 1:
            if k % 2:
                k = k * 3 + 1
            else:
                k //= 2
            arr.append(k)
        return arr
    graph = lothar(k)
    n = len(graph) - 1
    for a, b in ranges:
        s, e = a, n + b
        integral = 0
        if s <= e:
            for i in range(s + 1, e + 1):
                integral += (graph[i - 1] + graph[i]) / 2
        else:
            integral = -1
        ans.append(integral)
    return ans
