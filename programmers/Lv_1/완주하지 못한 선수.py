def solution(participant, completion):
    tmp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        print(hash(part))
        tmp += int(hash(part))
    for com in completion:
        tmp -= hash(com)
    answer = dic[tmp]
    return answer
