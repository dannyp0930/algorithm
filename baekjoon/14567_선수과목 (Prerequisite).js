const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, M] = input.shift().split(" ").map(Number);
const subjects = input.map((x) => x.split(" ").map(Number));

function solution(N, M, subjects) {
  const graph = Array.from({ length: N + 1 }, () => []);
  const indegree = Array(N + 1).fill(0);
  const semester = Array(N + 1).fill(1);
  for (let i = 0; i < M; i++) {
    const [A, B] = subjects[i];
    graph[A].push(B);
    indegree[B]++;
  }
  const queue = [];
  for (let i = 1; i <= N; i++) {
    if (indegree[i] === 0) queue.push(i);
  }
  while (queue.length) {
    const now = queue.shift();
    for (const next of graph[now]) {
      indegree[next]--;
      semester[next] = Math.max(semester[next], semester[now] + 1);
      if (indegree[next] === 0) {
        queue.push(next);
      }
    }
  }
  console.log(semester.slice(1).join(" "));
}

solution(N, M, subjects);
