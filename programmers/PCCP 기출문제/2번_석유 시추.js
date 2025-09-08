function solution(land) {
    const n = land.length;
    const m = land[0].length;
    const dr = [1, -1, 0, 0];
    const dc = [0, 0, 1, -1];
    const visit = Array.from(Array(n), () => Array(m).fill(false));
    const oils = Array(m).fill(0);
    const inside = (r, c) => {
        return 0 <= r && r < n && 0 <= c && c < m;
    }
    const bfs = (i, j) => {
        const queue = [[i, j]];
        visit[i][j] = true;
        let res = 0;
        const colSet = new Set();
        while (queue.length) {
            const [r, c] = queue.shift();
            res++;
            colSet.add(c);
            for (let d = 0; d < 4; d++) {
                const [nr, nc] = [r + dr[d], c + dc[d]];
                if (inside(nr, nc) && land[nr][nc] && !visit[nr][nc]) {
                    queue.push([nr, nc]);
                    visit[nr][nc] = true;
                }
            }
        }
        for (let col of colSet) {
            oils[col] += res;
        }
    }
    for (let r = 0; r < n; r++) {
        for (let c = 0; c < m; c++) {
            if (land[r][c] && !visit[r][c]) {
                bfs(r, c);
            }
        }
    }
    return Math.max(...oils);
}