const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const A = input[1].split(" ").map(Number);

function solution(N, A) {
  const dp = Array(N + 1).fill(0);
  for (let i = 1; i <= N; i++) {
    let max = A[i - 1];
    let min = A[i - 1];
    for (let j = i; j >= 1; j--) {
      if (max < A[j - 1]) max = A[j - 1];
      if (min > A[j - 1]) min = A[j - 1];
      dp[i] = Math.max(dp[i], dp[j - 1] + (max - min));
    }
  }
  console.log(dp[N]);
}

solution(N, A);
