# 기존 풀이
def solution1(brown, yellow):
    # 가능한 노란색 사각형의 높이와 너비
    candi = []
    for i in range(1, yellow + 1):
        if not yellow % i:
            candi.append([i, yellow // i])
    for m, n in candi:
        # 전체 카펫의 높이와 너비
        h = m + 2
        w = n + 2
        # 전체 면적 일치 여부
        if h * w == brown + yellow:
            return [w, h]


# 간략화
def solution2(brown, yellow):
    for i in range(1, int(yellow ** 0.5) + 1):
        if not yellow % i:
            h, w = i + 2, yellow // i + 2
            if h * w == brown + yellow:
                return [w, h]
