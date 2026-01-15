const fs = require("fs");
const n = Number(
  fs
    .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
    .toString()
    .trim()
);

function solution(n) {
  const dp = Array(n + 1).fill(0n);
  dp[0] = 1n;
  for (let i = 1; i <= n; i++) {
    for (let j = 0; j < i; j++) {
      dp[i] += dp[j] * dp[i - j - 1];
    }
  }
  console.log(dp[n].toString());
}

solution(n);
