const fs = require("fs");
const [S, K] =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split(" ").map(Number)
    : fs.readFileSync("input.txt").toString().trim().split(" ").map(Number);

function solution(S, K) {
  const a = (S / K) >> 0;
  const r = S % K;
  let answer = 1;
  for (let i = 0; i < r; i++) answer *= a + 1;
  for (let i = 0; i < K - r; i++) answer *= a;
  console.log(answer);
}

solution(S, K);
