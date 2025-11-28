const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const edges = input.slice(1, N).map((x) => x.split(" ").map(Number));
const q = Number(input[N]);
const questions = input.slice(N + 1).map((x) => x.split(" ").map(Number));

function solution(N, edges, q, questions) {
  const degree = Array(N + 1).fill(0);
  for (const [a, b] of edges) {
    degree[a]++;
    degree[b]++;
  }
  const res = [];
  for (const [t, k] of questions) {
    if (t === 1) {
      res.push(degree[k] >= 2 ? "yes" : "no");
    } else {
      res.push("yes");
    }
  }
  console.log(res.join("\n"));
}

solution(N, edges, q, questions);
