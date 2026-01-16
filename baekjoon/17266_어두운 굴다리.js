const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const M = Number(input[1]);
const X = input[2].split(" ").map(Number);

function solution(N, M, X) {
  let [s, e] = [1, N];
  let answer = N;

  const check = (h) => {
    if (X[0] > h) return false;
    for (let i = 0; i < M; i++) {
      if (X[i] - X[i - 1] > h * 2) return false;
    }
    if (X[M - 1] + h < N) return false;
    return true;
  };

  while (s <= e) {
    const m = (s + e) >> 1;
    if (check(m)) {
      answer = m;
      e = m - 1;
    } else s = m + 1;
  }

  console.log(answer);
}

solution(N, M, X);
