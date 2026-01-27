const fs = require("fs");
const n = Number(
  fs
    .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
    .toString()
    .trim(),
);

function solution(n) {
  const dp = Array(n).fill(0n);
  dp[0] = 1n;
  dp[1] = 1n;
  dp[2] = 1n;
  for (let i = 3; i < n; i++) {
    dp[i] = dp[i - 1] + dp[i - 3];
  }
  console.log(dp[n - 1].toString());
}

solution(n);
