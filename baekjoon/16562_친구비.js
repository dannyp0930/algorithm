const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, M, k] = input.shift().split(" ").map(Number);
const A = [0, ...input.shift().split(" ").map(Number)];
const edges = input.map((x) => x.split(" ").map(Number));

function solution(N, M, k, A, edges) {
  const parent = Array.from({ length: N + 1 }, (_, i) => i);
  const find = (x) => {
    if (parent[x] === x) return x;
    parent[x] = find(parent[x]);
    return parent[x];
  };
  const union = (a, b) => {
    const rootA = find(a);
    const rootB = find(b);
    if (rootA === rootB) return;
    if (A[rootA] <= A[rootB]) parent[rootB] = rootA;
    else parent[rootA] = rootB;
  };
  for (const [v, w] of edges) {
    union(v, w);
  }
  const visited = new Set();
  let total = 0;
  for (let i = 1; i <= N; i++) {
    const root = find(i);
    if (!visited.has(root)) {
      visited.add(root);
      total += A[root];
    }
  }
  console.log(total <= k ? total : "Oh no");
}

solution(N, M, k, A, edges);
