const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const A = input[1].split(" ").map(Number);

function solution(N, A) {
  let [l, r] = [0, N - 1];
  let B = Infinity;
  while (l < r) {
    const sum = A[l] + A[r];
    if (Math.abs(sum) < Math.abs(B)) B = sum;
    if (sum === 0) break;
    if (sum < 0) l++;
    else r--;
  }
  console.log(B);
}

solution(N, A);
