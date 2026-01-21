const fs = require("fs");
const n = BigInt(
  fs
    .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
    .toString()
    .trim(),
);

function solution(n) {
  let [s, e] = [0n, n];
  let answer = 0n;
  while (s <= e) {
    const mid = (s + e) / 2n;
    if (mid * mid >= n) {
      answer = mid;
      e = mid - 1n;
    } else {
      s = mid + 1n;
    }
  }
  console.log(answer.toString());
}

solution(n);
