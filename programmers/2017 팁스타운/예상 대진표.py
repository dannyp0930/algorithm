def solution(N, A, B):
    answer = 0
    # 번호를 1씩 제거하여 몫으로 계산
    A -= 1
    B -= 1
    while A != B:
        answer += 1
        A //= 2
        B //= 2
    return answer