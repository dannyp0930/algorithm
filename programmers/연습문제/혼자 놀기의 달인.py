def solution(cards):
    n = len(cards)
    start = cards[0]
    boxes = []
    visit = [0] * (n + 1)
    for i in range(n):
        if not visit[i + 1]:
            s = cards[i]
            cnt = 1
            stack = [s]
            visit[s] = 1
            while stack:
                n = stack.pop()
                e = cards[n - 1]
                if not visit[e]:
                    visit[e] = 1
                    stack.append(e)
                    cnt += 1
            boxes.append(cnt)
    boxes.sort(reverse=True)
    if len(boxes) > 1:
        return boxes[0] * boxes[1]
    return 0
