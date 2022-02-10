def solution(clothes):
    answer = 1
    dic = {}
    for c in clothes:
        if c[1] in dic.keys():
            dic[c[1]] += 1
        else:
            dic[c[1]] = 1
    for num in dic.values():
        answer *= (num + 1)
    return answer - 1
