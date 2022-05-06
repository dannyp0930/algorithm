def solution(files):
    answer = []
    tmp = []
    for file in files:
        head = ''
        number = ''
        tail = ''
        for i in range(len(file)):
            if file[i].isdigit():
                head, number = file[:i], file[i:]
                break
        for j in range(len(number)):
            if not number[j].isdigit():
                number, tail = number[:j], number[j:]
                break
        tmp.append([head, number, tail])
    tmp.sort(key=lambda x: (x[0].lower(), int(x[1])))
    for h, n, t in tmp:
        answer.append(h + n + t)
    return answer
