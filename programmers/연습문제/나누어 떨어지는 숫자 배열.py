def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor: continue
        answer.append(num)
        answer.sort()
    if not answer:
        answer = [-1]
    return answer
