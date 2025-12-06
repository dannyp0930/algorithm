const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, K] = input[0].split(" ").map(Number);
const S = input.slice(1).map((x) => x.split(" ").map(Number));

function solution(N, K, S) {
  const dp = Array.from({ length: K + 1 }, () => Array(N + 1).fill(0));
  for (let i = 1; i <= K; i++) {
    const [I, T] = S[i - 1];
    for (let t = 0; t <= N; t++) {
      dp[i][t] = dp[i - 1][t];
      if (t >= T) {
        dp[i][t] = Math.max(dp[i][t], dp[i - 1][t - T] + I);
      }
    }
  }
  console.log(dp[K][N]);
}

solution(N, K, S);
