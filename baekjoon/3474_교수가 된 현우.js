const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim()
  .split("\n");

function solution(input) {
  const T = Number(input[0]);
  const res = [];
  for (let t = 1; t <= T; t++) {
    const N = Number(input[t]);
    let cnt = 0;
    for (let i = 5; i <= N; i *= 5) {
      cnt += (N / i) >> 0;
    }
    res.push(cnt);
  }
  console.log(res.join("\n"));
}

solution(input);
