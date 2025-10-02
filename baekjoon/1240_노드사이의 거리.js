const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution() {
  const [N, M] = input[0].split(" ").map(Number);
  const graph = Array.from(Array(N + 1), () => []);
  for (let i = 1; i < N; i++) {
    const [s, e, w] = input[i].split(" ").map(Number);
    graph[s].push([e, w]);
    graph[e].push([s, w]);
  }
  const dfs = (n, cur, visit) => {
    if (visit[n]) return;
    visit[n] = cur;
    for (const [v, w] of graph[n]) {
      dfs(v, cur + w, visit);
    }
  };
  for (let i = N; i < N + M; i++) {
    const [s, e] = input[i].split(" ").map(Number);
    const visit = Array(N + 1).fill(0);
    dfs(s, 1, visit);
    console.log(visit[e] - 1);
  }
}

solution();
