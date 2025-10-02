const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const T = Number(input[0]);

function solution() {
  const dp = Array.from(Array(10001), () => Array(3).fill(0));
  (dp[1][0] = 1), (dp[2][0] = 1), (dp[2][1] = 1);
  (dp[3][0] = 1), (dp[3][1] = 1), (dp[3][2] = 1);
  for (let i = 4; i <= 10000; i++) {
    dp[i][0] = dp[i - 1][0];
    dp[i][1] = dp[i - 2][0] + dp[i - 2][1];
    dp[i][2] = dp[i - 3][0] + dp[i - 3][1] + dp[i - 3][2];
  }
  for (let i = 1; i <= T; i++) {
    const n = Number(input[i]);
    console.log(dp[n][0] + dp[n][1] + dp[n][2]);
  }
}

solution();
