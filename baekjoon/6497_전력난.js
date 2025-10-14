const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function kruscal(m, edges) {
  edges.sort((a, b) => a[2] - b[2]);
  const parent = Array.from({ length: m }, (_, i) => i);
  const find = (x) => (parent[x] === x ? x : (parent[x] = find(parent[x])));
  const union = (a, b) => {
    (a = find(a)), (b = find(b));
    if (a < b) parent[b] = a;
    else parent[a] = b;
  };
  let res = 0;
  for (const [x, y, z] of edges) {
    if (find(x) !== find(y)) {
      union(x, y);
    } else res += z;
  }
  return res;
}

function solution() {
  let i = 0;
  while (true) {
    const [m, n] = input[i].split(" ").map(Number);
    if (!m && !n) break;
    const edges = input
      .slice(i + 1, i + n + 1)
      .map((x) => x.split(" ").map(Number));
    console.log(kruscal(m, edges));
    i += n + 1;
  }
}

solution();
