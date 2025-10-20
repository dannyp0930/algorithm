const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, K] = input[0].split(" ").map(Number);
const H = input[1].split(" ").map(Number);

function solution(N, K, H) {
  const diff = Array(N - 1).fill(0);
  for (let i = 0; i < N - 1; i++) {
    diff[i] = H[i + 1] - H[i];
  }
  diff.sort((a, b) => a - b);
  const res = diff.slice(0, N - K).reduce((a, c) => a + c, 0);
  console.log(res);
}

solution(N, K, H);
