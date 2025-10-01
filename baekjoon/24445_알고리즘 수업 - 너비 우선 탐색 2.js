const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

class Queue {
    constructor() {
        this.items = {};
        this.first = 0;
        this.last = 0;
    }
    push(item) {
        this.items[this.last] = item;
        this.last++;
    }
    popleft() {
        if (!this.size()) return undefined;
        const item = this.items[this.first];
        delete this.items[this.first];
        this.first++;
        return item;
    }
    size() {
        return this.last - this.first;
    }
}

function solution() {
  const [N, M, R] = input[0].split(" ").map(Number);
  const graph = Array.from(Array(N + 1), () => []);
  for (let i = 1; i <= M; i++) {
    const [u, v] = input[i].split(" ").map(Number);
    graph[u].push(v);
    graph[v].push(u);
  }
  for (const arr of graph) {
    arr.sort((a, b) => b - a);
  }
  const visit = Array(N + 1).fill(0);
  const queue = new Queue();
  queue.push(R);
  let cnt = 1;
  visit[R] = cnt;
  while (queue.size()) {
    const node = queue.popleft();
    for (const vertex of graph[node]) {
        if (!visit[vertex]) {
            visit[vertex] = ++cnt;
            queue.push(vertex);
        }
    }
  }
  for (let i = 1; i <= N; i++) {
    console.log(visit[i]);
  }
}

solution();
