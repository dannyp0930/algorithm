def solution(n, times):
    answer = 0
    # 최소, 최대 시간
    left, right = min(times), max(times) * n

    # 같아질 때 까지 반복
    while left <= right:
        # 중간 시간
        mid = (left + right) // 2
        # 중간 시간동안 처리할 수 있는 인원 수
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break
        # 처리할 수 있는 인원이 n보다 크거나 같다면
        if people >= n:
            # 시간 저장, 최대값 줄이기
            answer = mid
            right = mid - 1
        else:
            # 최소값 늘리기
            left = mid + 1
    return answer


print(solution(6, [7, 10]))
