def solution(s):
    answer = []
    s = s[2:len(s) - 2]
    lst = s.split('},{')
    lst.sort(key=lambda x: len(x))
    lst = [list(map(int, val.split(','))) for val in lst]
    for arr in lst:
        for num in arr:
            if num not in answer:
                answer.append(num)
    return answer


string = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(string))
