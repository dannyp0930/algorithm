function solution(n, q, ans) {
    let answer = 0;
    const m = q.length;
    const comb = (r) => {
        let res = [];
        const dfs = (arr, idx) => {
            if (arr.length === r) {
                res.push([...arr]);
                return;
            }
            for (let i = idx; i < n; i++) {
                arr.push(i + 1);
                dfs(arr, i + 1);
                arr.pop();
            }
        }
        dfs([], 0);
        return res;
    }
    const candidates = comb(5);
    candidates.forEach((candi) => {
        let possible = true;
        for (let i = 0; i < m; i++) {
            let cnt = 0;
            for (let j = 0; j < 5; j++) {
                if (candi.includes(q[i][j])) cnt++;
            }
            if (cnt !== ans[i]) {
                possible = false;
                break;
            }
        }
        if (possible) answer++;
    });
    return answer;
}