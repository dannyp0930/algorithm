from collections import defaultdict


def solution(tickets):
    answer = []
    tickets.sort(key=lambda x: x[1], reverse=True)
    dic = defaultdict(list)
    for d, a in tickets:
        dic[d].append(a)

    def dfs():
        stack = ["ICN"]
        while stack:
            depart = stack[-1]
            if not dic[depart]:
                answer.append(stack.pop())
            else:
                stack.append(dic[depart].pop())
    dfs()
    return answer[::-1]
