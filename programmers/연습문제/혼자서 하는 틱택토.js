function solution(board) {
    let first = 0;
    let second = 0;
    const complete = (chr) => {
        for (let i = 0; i < 3; i++) {
            if (board[i][0] === chr && board[i][1] === chr && board[i][2] === chr) return true;
            if (board[0][i] === chr && board[1][i] === chr && board[2][i] === chr) return true;
        }
        if (board[0][0] === chr && board[1][1] === chr && board[2][2] === chr) return true;
        if (board[2][0] === chr && board[1][1] === chr && board[0][2] === chr) return true;
        return false;
    }
    board.forEach((b) => {
        first += b.split('O').length - 1;
        second += b.split('X').length - 1;
    });
    return (first - second === 1 && !complete('X') || first === second && !complete('O')) ? 1 : 0;
}