def solution(board):
    R, C = len(board), len(board[0])
    for r in range(1, R):
        for c in range(1, C):
            if board[r][c]:
                board[r][c] = min(board[r - 1][c - 1], board[r - 1][c], board[r][c - 1]) + 1
    max_length = 0
    for arr in board:
        max_length = max(max_length, max(arr))
    return max_length ** 2
