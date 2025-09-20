function solution(n, s, a, b, fares) {
    const graph = Array.from({ length: n + 1 }, () => Array());
    const dp = Array.from(Array(n + 1), () => Array(n + 1).fill(Infinity));
    for (let i = 1; i <= n; i++) {
        dp[i][i] = 0;
    }
    fares.forEach(([a, b, weight]) => {
        graph[a].push([b, weight]);
        graph[b].push([a, weight]);
        dp[a][b] = weight;
        dp[b][a] = weight;
    });
    for (let k = 1; k <= n; k++) {
        for (let i = 1; i <= n; i++) {
            for (let j = 1; j <= n; j++) {
                if (dp[i][j] > dp[i][k] + dp[k][j]) {
                    dp[i][j] = dp[i][k] + dp[k][j];
                }
            }
        }
    }
    let answer = dp[s][a] + dp[s][b];
    for (let i = 1; i <= n; i++) {
        const shared = dp[s][i] + dp[i][a] + dp[i][b];
        if (answer > shared) {
            answer = shared;
        }
    }
    return answer;
}