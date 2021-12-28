def determine(lst, arr):
    if not lst:
        return 1
    while lst:
        r, c = lst.pop()
        for nr, nc in lst:
            if abs(nr - r) + abs(nc - c) == 1:
                return 0
            if abs(nr - r) + abs(nc - c) == 2:
                if nr == r:
                    if arr[r][(c + nc) // 2] == 'O':
                        return 0
                elif nc == c:
                    if arr[(r + nr) // 2][c] == 'O':
                        return 0
                else:
                    if nr < r and nc < c:
                        if arr[r - 1][c] == 'O' or arr[r][c - 1] == 'O':
                            return 0
                    elif nr < r and nc > c:
                        if arr[r - 1][c] == 'O' or arr[r][c + 1] == 'O':
                            return 0
                    elif nr > r and nc < c:
                        if arr[r][c - 1] == 'O' or arr[r + 1][c] == 'O':
                            return 0
                    else:
                        if arr[r][c + 1] == 'O' or arr[r + 1][c] == 'O':
                            return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        candi = []
        for r in range(5):
            for c in range(5):
                if place[r][c] == 'P':
                    candi.append((r, c))
        answer.append(determine(candi, place))
    return answer
