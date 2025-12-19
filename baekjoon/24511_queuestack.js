const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const A = input[1].split(" ").map(Number);
const B = input[2].split(" ").map(Number);
const M = Number(input[3]);
const C = input[4].split(" ").map(Number);

function solution(N, A, B, M, C) {
  const queue = [];
  for (let i = 0; i < N; i++) {
    if (A[i] === 0) {
      queue.push(B[i])
    }
  }
  queue.reverse()
  console.log([...queue, ...C].slice(0, M).join(' '))

}

solution(N, A, B, M, C);
