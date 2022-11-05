def solution(string):
    stack = []
    i = 0
    for i in range(len(string)):
        stack.append(string[i])
        if stack[-4:] == list('PPAP'):
            for _ in range(3):
                stack.pop()
    if stack == ['P', 'P', 'A', 'P'] or stack == ['P']:
        return 'PPAP'
    return 'NP'


string = input()
print(solution(string))
