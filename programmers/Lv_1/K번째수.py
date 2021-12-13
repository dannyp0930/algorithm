def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        lst = array[i - 1:j]
        lst.sort()
        num = lst[k - 1]
        answer.append(num)
    return answer
