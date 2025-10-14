const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const T = Number(input.shift());

function solution(T, input) {
  let i = 0;
  while (T) {
    const N = +input[i];
    const edges = input
      .slice(i + 1, i + N)
      .map((x) => x.split(" ").map(Number));
    const target = input[i + N].split(" ").map(Number);
    const parent = Array(N + 1).fill(0);
    for (const [a, b] of edges) {
      parent[b] = a;
    }
    const lca = (a, b) => {
      const visit = new Set();
      while (a) {
        visit.add(a)
        a = parent[a]
      }
      while (b) {
        if (visit.has(b)) return b;
        b = parent[b];
      }
    };
    console.log(lca(...target));
    i += N + 1;
    T--;
  }
}

solution(T, input);
