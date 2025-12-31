const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const A = input[1].split(" ").map(Number);
const M = Number(input[2]);
const arr = input.slice(3).map((x) => x.split(" ").map(Number));

function solution(N, A, M, arr) {
  const prefix = Array(N + 1).fill(0);
  for (let i = 0; i < N; i++) {
    prefix[i + 1] = prefix[i] + A[i];
  }
  const res = [];
  for (let i = 0; i < M; i++) {
    const [s, e] = arr[i];
    res.push(prefix[e] - prefix[s - 1]);
  }
  console.log(res.join("\n"));
}

solution(N, A, M, arr);
