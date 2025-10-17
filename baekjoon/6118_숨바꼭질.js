const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, _M] = input.shift().split(" ").map(Number);
const edges = input.map((x) => x.split(" ").map(Number));

function solution(N, edges) {
  const graph = Array.from({ length: N + 1 }, () => []);
  const visited = Array(N + 1).fill(-1);
  for (const [a, b] of edges) {
    graph[a].push(b);
    graph[b].push(a);
  }
  const queue = [1];
  visited[1] = 0;
  while (queue.length) {
    const cur = queue.shift();
    for (const next of graph[cur]) {
      if (visited[next] === -1) {
        visited[next] = visited[cur] + 1;
        queue.push(next);
      }
    }
  }
  let answer = [0, 0, 0];
  for (let i = 1; i <= N; i++) {
    if (answer[1] < visited[i]) {
      answer = [i, visited[i], 1];
    } else if (answer[1] === visited[i]) {
      answer[2]++;
    }
  }
  console.log(...answer);
}

solution(N, edges);
