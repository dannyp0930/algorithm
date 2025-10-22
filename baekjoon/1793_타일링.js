const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n").map(Number)
    : fs.readFileSync("input.txt").toString().trim().split("\n").map(Number);

function solution() {
  const dp = Array(251).fill(0n);
  dp[0] = 1n;
  dp[1] = 1n;
  for (let i = 2; i <= 250; i++) {
    dp[i] = dp[i - 1] + 2n * dp[i - 2];
  }
  for (const n of input) {
    console.log(dp[n].toString());
  }
}

solution();
