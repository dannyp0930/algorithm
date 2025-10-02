const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution() {
  const [M, N] = input.shift().split(" ").map(Number);
  const graph = input.map((a) => a.split(" ").map(Number));
  const dp = Array.from(Array(M), () => Array(N).fill(-1));
  const dr = [1, -1, 0, 0];
  const dc = [0, 0, 1, -1];
  const possible = (nr, nc, r, c) => {
    return (
      nr >= 0 && nc >= 0 && nr < M && nc < N && graph[r][c] > graph[nr][nc]
    );
  };
  const dfs = (r, c) => {
    if (r === M - 1 && c === N - 1) return 1;
    if (dp[r][c] !== -1) return dp[r][c];
    let cnt = 0;
    for (let d = 0; d < 4; d++) {
      const [nr, nc] = [r + dr[d], c + dc[d]];
      if (possible(nr, nc, r, c)) {
        cnt += dfs(nr, nc);
      }
    }
    dp[r][c] = cnt;
    return dp[r][c];
  };
  console.log(dfs(0, 0));
}

solution();
