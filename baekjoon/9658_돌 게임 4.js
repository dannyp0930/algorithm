const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim()
    : fs.readFileSync("input.txt").toString().trim();

const N = +input;

function solution(N) {
  const dp = Array(N + 1).fill(false);
  dp[2] = true;
  dp[4] = true;
  for (let i = 5; i <= N; i++) {
    if (!dp[i - 1] || !dp[i - 3] || !dp[i - 4]) dp[i] = true;
  }
  console.log(dp[N] ? "SK" : "CY");
}

solution(N);
