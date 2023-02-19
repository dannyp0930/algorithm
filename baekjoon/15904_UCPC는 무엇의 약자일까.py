def solution():
    ucpc = 'UCPC'
    idx = 0
    res = ''
    for word in arr:
        if 64 < ord(word[0]) < 91:
            if word[0] == ucpc[idx]:
                res += word[0]
                idx += 1
        if idx == 4:
            return 'I love UCPC'
    return 'I hate UCPC'
    

arr = list(input().replace(' ', ''))
print(solution())
