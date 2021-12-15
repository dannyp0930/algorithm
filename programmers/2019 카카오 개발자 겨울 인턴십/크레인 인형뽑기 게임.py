def solution(board, moves):
    answer = 0
    size = len(board[0])
    result = []
    for c in moves:
        for r in range(size):
            if board[r][c - 1]:
                doll = board[r][c - 1]
                if not result or result[-1] != doll:
                    result.append(doll)
                else:
                    result.pop()
                    answer += 2
                board[r][c - 1] = 0
                break
    return answer
