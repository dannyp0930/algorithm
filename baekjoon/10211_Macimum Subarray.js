const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim()
  .split("\n");

function solution(input) {
  let T = input[0];
  let idx = 1;
  const res = [];
  while (T--) {
    const N = input[idx++];
    const X = input[idx++].split(" ").map(Number);
    const dp = Array(N).fill(0);
    dp[0] = X[0];
    for (let i = 1; i < N; i++) {
      dp[i] = Math.max(X[i], dp[i - 1] + X[i]);
    }
    res.push(Math.max(...dp));
  }
  console.log(res.join("\n"));
}

solution(input);
