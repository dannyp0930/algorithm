def solution(s):
    words = s.split(' ')
    change = []
    for word in words:
        N = len(word)
        tmp = ''
        for i in range(N):
            if i:
                tmp += word[i].lower()
            else:
                tmp += word[i].upper()
        change.append(tmp)
    return ' '.join(change)
