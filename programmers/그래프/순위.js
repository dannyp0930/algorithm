function solution(n, results) {
    let answer = 0;
    const graph = Array.from(Array(n + 1), () => Array(n + 1).fill(false));
    results.forEach(([a, b]) => {
        graph[a][b] = true; 
    });
    for (let k = 1; k <= n; k++) {
        for (let a = 1; a <= n; a++) {
            for (let b = 1; b <= n; b++) {
                if (graph[a][k] && graph[k][b]) graph[a][b] = true;
            }
        }
    }
    for (let i = 1; i <= n; i++) {
        let cnt = 0;
        for (let j = 1; j <= n; j++) {
            if (graph[i][j] || graph[j][i]) {
                cnt++;
            }
        }
        if (cnt === n - 1) answer++;
    }
    return answer;
}