def solution(want, number, discount):
    answer = 0
    dic = {want[i]: number[i] for i in range(len(want))}
    days = len(discount)
    for i in range(days - 9):
        tmp = {}
        for p in discount[i: i + 10]:
            if p in tmp:
                tmp[p] += 1
            else:
                tmp[p] = 1
        if tmp == dic:
            answer += 1
    return answer
