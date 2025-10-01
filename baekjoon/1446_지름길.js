const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution() {
  const [_N, D] = input.shift().split(" ").map(Number);
  const shortCuts = input
    .map((x) => x.split(" ").map(Number))
    .sort((a, b) => (a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]));
  const dp = Array(D + 1).fill(0);
  for (let i = 1; i <= D; i++) {
    dp[i] = dp[i - 1] + 1;
    for (const [s, e, w] of shortCuts) {
      if (e === i) {
        dp[e] = dp[e] > dp[s] + w ? dp[s] + w : dp[e];
      }
    }
  }
  console.log(dp[D]);
}

solution();
