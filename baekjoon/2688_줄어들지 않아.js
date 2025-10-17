const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

input.shift();
const dp = Array.from({ length: 65 }, () => Array(10).fill(0));
for (let i = 0; i < 10; i++) dp[1][i] = 1;
for (let j = 2; j <= 64; j++) {
  for (let k = 0; k < 10; k++) {
    dp[j][k] = dp[j - 1].slice(k, 10).reduce((a, c) => a + c);
  }
}

const arr = input.map(Number);

function solution(arr) {
  for (const num of arr) {
    console.log(dp[num].reduce((a, c) => a + c));
  }
}

solution(arr);
