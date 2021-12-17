def solution(s):
    words = []
    for word in s.split(' '):
        change = ''
        for i in range(len(word)):
            if i % 2:
                change += word[i].lower()
            else:
                change += word[i].upper()
        words.append(change)
    return ' '.join(words)
