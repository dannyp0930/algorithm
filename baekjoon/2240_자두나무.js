const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [T, W] = input.shift().split(" ").map(Number);
const plums = [0, ...input.map(Number)];

function solution() {
  const dp = Array.from(Array(T + 1), () => Array(W + 1).fill(0));
  for (let t = 1; t <= T; t++) {
    dp[t][0] = dp[t - 1][0] + (plums[t] % 2);
    for (let w = 1; w <= W; w++) {
      const cnt = w % 2 ? plums[t] >> 1 : plums[t] % 2;
      dp[t][w] = Math.max(dp[t - 1][w], dp[t - 1][w - 1]) + cnt;
    }
  }
  console.log(Math.max(...dp[T]));
}

solution();
