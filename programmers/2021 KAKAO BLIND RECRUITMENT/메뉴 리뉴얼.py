from itertools import combinations


def solution(orders, course):
    answer = []
    n = len(course)

    # 각 코스요리의 개수만큼 만들어질 수 있는 코스
    dic_list = [{} for _ in range(n)]

    # 각 주문에서
    for order in orders:
        # 조합으로 코스 생성
        for i in range(n):
            for ch in combinations(order, course[i]):
                tmp = ''.join(sorted(ch))
                if tmp in dic_list[i]:
                    dic_list[i][tmp] += 1
                else:
                    dic_list[i][tmp] = 1

    for d in dic_list:
        # 코스가 생성되지 않았으면 종료
        if not d:
            break
        # 최댓값 찾기
        cnt = 0
        temp = []
        for k, v in d.items():
            # 주문한 손님이 2명 이하라면 넘어간다
            if v < 2: continue
            if v > cnt:
                cnt = int(v)
                temp = [k]
            elif v == cnt:
                temp.append(k)
        for c in temp:
            answer.append(c)
        answer.sort()
    return answer
