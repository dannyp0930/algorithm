const fs = require("fs");
const N = Number(
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim()
    : fs.readFileSync("input.txt").toString().trim()
);

function solution(N) {
  const len = [3];
  let k = 0;
  while (len[k] < N) {
    len.push(len[k] * 2 + k + 4);
    k++;
  }

  const find = (k, n) => {
    if (k === 0) return n === 1 ? "m" : "o";
    const left = len[k - 1];
    const mid = k + 3;
    if (n <= left) return find(k - 1, n);
    if (n <= left + mid) return n === left + 1 ? "m" : "o";
    return find(k - 1, n - left - mid);
  };

  console.log(find(k, N));
}

solution(N);
