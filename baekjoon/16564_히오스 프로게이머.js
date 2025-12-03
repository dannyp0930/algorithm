const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, K] = input[0].split(" ").map(Number);
const X = input.slice(1).map(Number);

function solution(N, K, X) {
  let [s, e] = [Math.min(...X), Math.max(...X) + K];
  while (s < e) {
    const mid = (s + e + 1) >> 1;
    let plus = 0;
    for (const x of X) {
      if (x < mid) plus += mid - x;
    }
    if (plus <= K) s = mid;
    else e = mid - 1;
  }
  console.log(s);
}

solution(N, K, X);
