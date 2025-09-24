function solution(n, m, x, y, r, c, k) {
    const dist = k - Math.abs(x - r) + Math.abs(y - c);
    if (dist < 0 || dist % 2) return "impossible";
    let answer = 'z'.repeat(k);
    const dr = [1, 0, 0, -1];
    const dc = [0, -1, 1, 0];
    const ds = ['d', 'l', 'r', 'u'];
    const dfs = (cnt, x, y, str, dist) => {
        if (cnt > k) return;
        if (dist > k) return;
        if (cnt === k && x === r && y === c && answer > str) {
            answer = str;
            return;
        }
        if (answer !== 'z'.repeat(k)) return;
        for (let d = 0; d < 4; d++) {
            const [nr, nc] = [x + dr[d], y + dc[d]];
            if (0 < nr && nr <= n && 0 < nc && nc <= m) {
                dfs(cnt + 1, nr, nc, str + ds[d], Math.abs(nr - r) + Math.abs(nc - c) + cnt + 1);
            }
        }
    }
    dfs(0, x, y, '', k);
    return answer === 'z'.repeat(k) ? 'impossible' : answer;
}