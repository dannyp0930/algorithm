const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [n, m] = input[0].split(" ").map(Number);
const boss = input[1].split(" ").map(Number);
const praise = input.slice(2, 2 + m).map((x) => x.split(" ").map(Number));

function solution(n, boss, praise) {
  const graph = Array.from({ length: n + 1 }, () => []);
  const dp = Array(n + 1).fill(0);
  for (let i = 1; i < n; i++) {
    graph[boss[i]].push(i + 1);
  }
  for (const [i, w] of praise) {
    dp[i] += w;
  }
  const dfs = (cur) => {
    for (const next of graph[cur]) {
      dp[next] += dp[cur];
      dfs(next);
    }
  };
  dfs(1);
  console.log(dp.slice(1).join(" "));
}

solution(n, boss, praise);
