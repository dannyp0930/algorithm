const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input.shift());

function solution(N, edges) {
  const graph = Array.from({ length: N + 1 }, () => []);
  for (const edge of edges) {
    const [a, b] = edge.split(" ").map(Number);
    graph[a].push(b);
    graph[b].push(a);
  }
  const depth = Array(N + 1).fill(-1);
  const stack = [[1, 0]];
  while (stack.length) {
    const [n, d] = stack.pop();
    if (depth[n] !== -1) continue;
    depth[n] = d;
    for (const v of graph[n]) {
      if (depth[v] === -1) stack.push([v, d + 1]);
    }
  }
  let cnt = 0;
  for (let i = 2; i <= N; i++) {
    if (graph[i].length === 1) cnt += depth[i];
  }
  console.log(cnt % 2 ? "Yes" : "No");
}

solution(N, input);
