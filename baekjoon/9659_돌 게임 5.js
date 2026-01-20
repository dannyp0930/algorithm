const fs = require("fs");
const N = BigInt(
  fs
    .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
    .toString()
    .trim()
);

function solution(N) {
  console.log(N % 2n === 1n ? "SK" : "CY");
}

solution(N);
