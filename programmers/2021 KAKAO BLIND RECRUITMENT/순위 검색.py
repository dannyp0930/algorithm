# 처음 방법, 효율성 테스트 실패
def solution1(info, query):
    answer = []

    applicant = []

    for arr in info:
        applicant.append(arr.split(' '))

    for t in query:
        t = t.split(' ')
        language = t[0]
        job = t[2]
        career = t[4]
        soul_food = t[6]
        score = int(t[7])
        tmp = 0

        for data in applicant:
            if language == '-' or language == data[0]:
                if job == '-' or job == data[1]:
                    if career == '-' or career == data[2]:
                        if soul_food == '-' or soul_food == data[3]:
                            if score <= int(data[4]):
                                tmp += 1

        answer.append(tmp)
    return answer


# 라이브러리 함수로 탐색, hash구조 이용
from itertools import combinations as comb
from bisect import bisect_left as bl


def solution2(info, query):
    answer = []

    # 정보를 key, value로 나누어 저장
    info_dict = {}
    for i in info:
        i = i.split()

        # 문자열 정보를 key로
        keys = i[:-1]

        # 점수를 value로
        value = int(i[-1])

        for j in range(5):
            # keys의 조합으로 key, value쌍으로 저장
            for k in comb(keys, j):
                tmp = ''.join(k)
                if tmp in info_dict:
                    info_dict[tmp].append(value)
                else:
                    info_dict[tmp] = [value]

    # value로 정렬
    for k in info_dict:
        info_dict[k].sort(reverse=True)

    # 조건으로 key생성
    for q in query:
        q = q.split()
        key = ''
        value = int(q[-1])
        q = q[:-1]

        for ch in q:
            # '-'인 경우 넘어간다
            if ch == '-' or ch == 'and':
                continue
            key += ch

        cnt = 0
        if key in info_dict:
            scores = info_dict[key]
            if scores:
                # 이분탐색 함수로 조건을 만족하는 사람 수 세기
                cnt = len(scores) - bl(scores, value)
        answer.append(cnt)
    return answer
