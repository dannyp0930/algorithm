function solution(storage, requests) {
    const n = storage.length;
    const m = storage[0].length;
    const visit = storage.map((store) => store.split(""));
    let ans = n * m;
    const inside = (r, c) => {
        return r >= 0 && r < n && c >= 0 && c < m;
    }
    const reachable = (r, c) => {
        const dr = [1, -1, 0, 0];
        const dc = [0, 0, 1, -1];
        for (let d = 0; d < 4; d++) {
            let [nr, nc] = [r + dr[d], c + dc[d]];
            if (nr < 0 || nr >= n || nc < 0 || nc >= m) {
                return true;
            } else if (inside(nr, nc) && visit[nr][nc] === true) {
                return true;
            }
        }
        return false;
    }
    const updateVisit = () => {
        for (let r = 0; r < n; r++) {
            for (let c = 0; c < m; c++) {
                if (reachable(r, c) && visit[r][c] === false) {
                    const queue = [[r, c]];
                    const dr = [1, -1, 0, 0];
                    const dc = [0, 0, 1, -1];
                    while (queue.length) {
                        const [r, c] = queue.shift();
                        visit[r][c] = true;
                        for (let d = 0; d < 4; d++) {
                            let [nr, nc] = [r + dr[d], c + dc[d]];
                            if (inside(nr, nc) && reachable(nr, nc) && visit[nr][nc] === false) {
                                queue.push([nr, nc]);
                            }
                        }
                    }
                }
            }
        }
    }
    requests.forEach((req, i) => {
        updateVisit();
        if (req.length === 1) {
            const lst = []
            for (let r = 0; r < n; r++) {
                for (let c = 0; c < m; c++) {
                    if (reachable(r, c) && visit[r][c] === req) {
                        lst.push([r, c]);
                    }
                }
            }
            lst.forEach(([r, c]) => {
                visit[r][c] = true;
                ans--;
            });
        } else {
            for (let r = 0; r < n; r++) {
                for (let c = 0; c < m; c++) {
                    if (visit[r][c] === req[0]) {
                        visit[r][c] = false;
                        ans--;
                    }
                }
            }
        }
    });
    return ans;
}