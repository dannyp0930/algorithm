function solution(board, skill) {
    const n = board.length;
    const m = board[0].length;
    const cum = Array.from({ length: n + 1 }, () => Array(m + 1).fill(0));
    skill.forEach(([type, r1, c1, r2, c2, degree]) => {
       if (type === 1) {
           cum[r1][c1] -= degree;
           cum[r1][c2 + 1] += degree;
           cum[r2 + 1][c1] += degree;
           cum[r2 + 1][c2 + 1] -= degree;
       } else {
           cum[r1][c1] += degree;
           cum[r1][c2 + 1] -= degree;
           cum[r2 + 1][c1] -= degree;
           cum[r2 + 1][c2 + 1] += degree;
       }
    });
    for (let r = 0; r < n; r++) {
        for (let c = 0; c <= m; c++) {
            cum[r + 1][c] += cum[r][c];
        }
    }
    for (let r = 0; r <= n; r++) {
        for (let c = 0; c < m; c++) {
            cum[r][c + 1] += cum[r][c];
        }
    }
    for (let r = 0; r < n; r++) {
        for (let c = 0; c < m; c++) {
            board[r][c] += cum[r][c];
        }
    }
    return board.reduce((a, b) => a + b.filter((x) => x > 0).length, 0);
}