const fs = require("fs");
const N = Number(
  fs
    .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
    .toString()
    .trim(),
);

function solution(N) {
  const values = [1, 5, 10, 50];
  const res = new Set();
  const backtrack = (idx, cnt, tot) => {
    if (cnt === N) {
      res.add(tot);
      return;
    }
    for (let i = idx; i < 4; i++) {
      backtrack(i, cnt + 1, tot + values[i]);
    }
  };
  backtrack(0, 0, 0);
  console.log(res.size);
}

solution(N);
