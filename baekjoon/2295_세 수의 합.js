const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input.shift());
const U = input.map(Number);

function solution(N, U) {
  U.sort((a, b) => b - a);
  const sumSet = new Set();
  for (let i = 0; i < N; i++) {
    for (let j = i; j < N; j++) {
        sumSet.add(U[i] + U[j])
    }
  }
  for (let i = 0; i < N; i++) {
    for (let j = i; j < N; j++) {
      if (sumSet.has(U[i] - U[j])) {
        return U[i];
      }
    }
  }
}

console.log(solution(N, U));
