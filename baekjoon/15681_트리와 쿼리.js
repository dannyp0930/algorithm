const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution() {
  const [N, R, Q] = input[0].split(" ").map(Number);
  const graph = Array.from(Array(N + 1), () => []);
  for (let i = 1; i < N; i++) {
    const [u, v] = input[i].split(" ").map(Number);
    graph[u].push(v);
    graph[v].push(u);
  }
  const dp = Array(N + 1).fill(0);
  const dfs = (node, prevNode) => {
    dp[node] = 1;
    for (const vertex of graph[node]) {
        if (vertex !== prevNode) {
            dfs(vertex, node);
            dp[node] += dp[vertex];
        }
    }
  }
  dfs(R, -1);
  for (let i = N; i < N + Q; i++) {
    console.log(dp[input[i]]);
  }
}

solution();
