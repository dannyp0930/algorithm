const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution() {
  const [N, M, R] = input[0].split(" ").map(Number);
  const graph = Array.from(Array(N + 1), () => []);
  const visit = Array(N + 1).fill(0);
  for (let i = 1; i <= M; i++) {
    const [u, v] = input[i].split(" ").map(Number);
    graph[u].push(v);
    graph[v].push(u);
  }
  for (const arr of graph) {
    arr.sort((a, b) => b - a);
  }
  const dfs = (cur) => {
    if (!visit[cur]) {
      visit[cur] = cnt;
      cnt++;
      for (const next of graph[cur]) {
        dfs(next);
      }
    }
  };
  let cnt = 1;
  dfs(R);
  for (let i = 1; i <= N; i++) {
    console.log(visit[i]);
  }
}

solution();
