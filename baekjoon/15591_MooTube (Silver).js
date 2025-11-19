const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, Q] = input[0].split(" ").map(Number);
const USADO = input.slice(1, N).map((x) => x.split(" ").map(Number));
const quests = input.slice(N, N + Q).map((x) => x.split(" ").map(Number));

function solution(N, USADO, quests) {
  const graph = Array.from({ length: N + 1 }, () => []);
  for (const [p, q, r] of USADO) {
    graph[p].push([q, r]);
    graph[q].push([p, r]);
  }
  for (const [k, v] of quests) {
    const visited = Array(N + 1).fill(false);
    let cnt = 0;
    const queue = [v];
    visited[v] = true;
    let head = 0;
    while (head < queue.length) {
      const node = queue[head++];
      for (const [next, weight] of graph[node]) {
        if (!visited[next] && weight >= k) {
          visited[next] = true;
          queue.push(next);
          cnt++;
        }
      }
    }
    console.log(cnt);
  }
}

solution(N, USADO, quests);
