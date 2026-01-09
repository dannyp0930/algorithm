const fs = require("fs");
const [N, K] = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .trim()
  .split(" ")
  .map(Number);

function solution(N, K) {
  const S = (K * (K + 1)) / 2;
  const left = N - S;
  if (left < 0) return -1;
  return left % K ? K : K - 1;
}

console.log(solution(N, K));
