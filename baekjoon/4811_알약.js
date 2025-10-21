const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n").map(Number)
    : fs.readFileSync("input.txt").toString().trim().split("\n").map(Number);

function solution() {
  const dp = Array.from({ length: 31 }, () => Array(31).fill(0));
  for (let w = 1; w <= 30; w++) {
    for (let h = 0; h <= 30; h++) {
      if (h > w) continue;
      if (h === 0) dp[w][h] = 1;
      else dp[w][h] = dp[w][h - 1] + dp[w - 1][h];
    }
  }
  const length = input.length;
  let t = 0;
  while (t < length - 1) {
    const N = input[t];
    console.log(dp[N][N]);
    t++;
  }
}

solution();
