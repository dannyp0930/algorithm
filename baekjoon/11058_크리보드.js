const fs = require("fs");
const N =
  process.platform === "linux"
    ? Number(fs.readFileSync(0, "utf-8").toString().trim())
    : Number(fs.readFileSync("input.txt").toString().trim());

function solution(N) {
  const dp = Array.from({ length: N + 1 }, (_, i) => i);
  for (let i = 4; i <= N; i++) {
    for (let j = 2; j <= i - 3; j++) {
      dp[i] = Math.max(dp[i], dp[j] * (i - j - 1));
    }
  }
  console.log(dp[N]);
}

solution(N);
