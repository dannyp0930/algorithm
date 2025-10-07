const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

class MinHeap {
  constructor() {
    this.data = [];
  }
  get size() {
    return this.data.length;
  }
  push(value) {
    this.data.push(value);
    this._siftUp();
  }
  pop() {
    if (!this.data.length) return undefined;
    const root = this.data[0];
    const last = this.data.pop();
    if (this.data.length) {
      this.data[0] = last;
      this._siftDown();
    }
    return root;
  }
  _siftUp() {
    let i = this.data.length - 1;
    while (i) {
      const p = (i - 1) >> 1;
      if (this.data[i][1] < this.data[p][1]) {
        this._swap(i, p);
      } else break;
    }
  }
  _siftDown() {
    const n = this.data.length;
    let i = 0;
    while (true) {
      const l = 2 * i + 1;
      const r = 2 * i + 2;
      let s = i;
      if (l < n && this.data[l][1] < this.data[s][1]) s = l;
      if (r < n && this.data[r][1] < this.data[s][1]) s = r;
      if (s === i) break;
      this._swap(i, s);
      i = s;
    }
  }
  _swap(a, b) {
    [this.data[a], this.data[b]] = [this.data[b], this.data[a]];
  }
}

function solution() {
  const [N, M] = input.shift().split(" ").map(Number);
  const graph = Array.from(Array(N + 1), () => []);
  for (let i = 0; i < M; i++) {
    const [A, B, C] = input[i].split(" ").map(Number);
    graph[A].push([B, C]);
    graph[B].push([A, C]);
  }
  const dist = Array(N + 1).fill(Infinity);
  const heap = new MinHeap();
  heap.push([1, 0]);
  dist[1] = 0;
  while (heap.size) {
    const [node, _cur] = heap.pop();
    for (const [vertex, weight] of graph[node]) {
      if (dist[node] + weight < dist[vertex]) {
        dist[vertex] = dist[node] + weight;
        heap.push([vertex, dist[vertex]]);
      }
    }
  }
  console.log(dist[N]);
}

solution();
