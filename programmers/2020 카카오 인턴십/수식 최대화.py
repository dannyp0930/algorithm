from itertools import permutations


def solution(expression):
    answer = 0
    operators = ["+", "-", "*"]
    for priority in permutations(operators):
        new = []
        # 먼저 우선순위가 낮은 연산자로 분리
        first = expression.split(priority[0])

        for sec in first:
            # 두 번째 우선순위 연산자로 분리하고
            second = sec.split(priority[1])

            # eval() 함수를 이용해 문자열을 계산값으로 변경
            second = [str(eval(x)) for x in second]

            # 두 번째 우선순위 연산자를 붙여 저장
            new.append(priority[1].join(second))

        # 각 값을 eval() 함수로 계산값으로 변경
        new = [str(eval(x)) for x in new]

        # 가장 낮은 우선순위로 묶고 계산값 도출
        result = abs(eval(priority[0].join(new)))

        # 최댓값 판별
        answer = max(answer, result)
    return answer
