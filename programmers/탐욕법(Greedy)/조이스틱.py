def solution(name):
    answer = 0
    N = len(name)
    # 좌우 움직임 순서대로 작성하는 경우
    min_move = N - 1

    # 상하 움직임 더하기
    for i, ch in enumerate(name):
        answer += min(ord(ch) - 65, 90 - ord(ch) + 1)

        # 오른쪽으로 이동후 뒤의 A의 개수 판별
        move = i + 1
        while move < N and name[move] == 'A':
            move += 1

        # 최솟값 판별
        # 1. 오른쪽으로 가다 A를 만나면 왼쪽으로
        # 2. 왼쪽으로 가다 A를 만나면 오른쪽으로
        min_move = min(min_move, i * 2 + N - move, (N - move) * 2 + i)

    answer += min_move
    return answer
