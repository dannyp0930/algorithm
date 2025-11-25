const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const A = input[1].split(" ").map(Number);
const B = input[2].split(" ").map(Number);

function solution(N, A, B) {
  const dp = Array.from({ length: N + 1 }, () => Array(N + 1).fill(0));
  for (let i = N - 1; i >= 0; i--) {
    for (let j = N - 1; j >= 0; j--) {
      if (A[i] > B[j]) {
        dp[i][j] = dp[i][j + 1] + B[j];
      } else {
        dp[i][j] = Math.max(dp[i + 1][j], dp[i + 1][j + 1]);
      }
    }
  }
  console.log(dp[0][0]);
}

solution(N, A, B);
