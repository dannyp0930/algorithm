const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n").map(Number)
    : fs.readFileSync("input.txt").toString().trim().split("\n").map(Number);

function solution(input) {
  const dp = [0, 1];
  dp[1] = 1;
  for (let i = 2; i < 45; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }
  input.shift();
  for (const n of input) {
    let idx = 44;
    let target = n;
    const res = [];
    while (target) {
      if (target >= dp[idx]) {
        res.push(dp[idx]);
        target -= dp[idx];
      }
      idx--;
    }
    console.log(res.sort((a, b) => a - b).join(" "));
  }
}

solution(input);
