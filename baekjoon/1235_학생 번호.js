const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const arr = input.slice(1);

function solution(N, arr) {
  const len = arr[0].length;
  for (let k = 1; k < len; k++) {
    const set = new Set();
    for (const no of arr) {
      set.add(no.slice(-k));
    }
    if (set.size === N) return k;
  }
  return len;
}

console.log(solution(N, arr));
