const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const bridge = input.slice(1).map((x) => x.split(" ").map(Number));

function solution(N, bridge) {
  const parent = Array.from({ length: N + 1 }, (_, i) => i);
  const find = (x) => {
    if (parent[x] === x) return x;
    return (parent[x] = find(parent[x]));
  };
  const union = (x, y) => {
    x = find(x);
    y = find(y);
    if (x === y) return;
    parent[y] = x;
  };
  for (const [a, b] of bridge) {
    union(a, b);
  }
  const root = find(1);
  for (let i = 2; i <= N; i++) {
    if (find(i) !== root) {
      console.log(1, i);
      return;
    }
  }
}

solution(N, bridge);
