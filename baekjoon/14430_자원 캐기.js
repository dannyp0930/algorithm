const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const ore = input.slice(1).map((x) => x.split(" ").map(Number));

function solution(N, M, ore) {
  const dp = Array.from({ length: N + 1 }, () => Array(M + 1).fill(0));
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      dp[i + 1][j + 1] = Math.max(dp[i][j + 1], dp[i + 1][j]) + ore[i][j];
    }
  }
  console.log(dp[N][M]);
}

solution(N, M, ore);
