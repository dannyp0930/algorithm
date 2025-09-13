function solution(board) {
    let answer = Infinity;
    const n = board.length;
    const dp = Array.from(Array(n), () => Array(n).fill(Infinity));
    const queue = [[0, 0, 0, -1]];
    const dr = [1, -1, 0, 0];
    const dc = [0, 0, 1, -1];
    while (queue.length) {
        const [r, c, cost, dir] = queue.shift();
        if (r === n - 1 && c === n - 1 && answer > cost) {
            answer = cost;
        }
        for (let d = 0; d < 4; d++) {
            const [nr, nc] = [r + dr[d], c + dc[d]];
            if (!(0 <= nr && nr < n && 0 <= nc && nc < n) || board[nr][nc]) continue;
            const plus = (dir === d || dir === -1) ? 1 : 6;
            if (dp[nr][nc] < cost + plus - 4) continue;
            dp[nr][nc] = cost + plus;
            queue.push([nr, nc, cost + plus, d]);   
        }
    }
    return answer * 100;
}