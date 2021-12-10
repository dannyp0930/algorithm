def solution(s):
    answer = ''
    num = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    tmp = ''
    for c in s:
        if c in num.values():
            answer += c
        else:
            tmp += c
            if tmp in num.keys():
                answer += num[tmp]
                tmp = ''
    return int(answer)
