const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [, T] = input.shift().split(" ").map(Number);
const units = input.map((x) => x.split(" ").map(Number));

function solution(T, units) {
  const dp = Array(T + 1).fill(0);
  for (const [K, S] of units) {
    for (let t = T; t >= K; t--) {
      dp[t] = Math.max(dp[t], dp[t - K] + S);
    }
  }
  console.log(dp[T]);
}

solution(T, units);
