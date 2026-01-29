const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const C = input.slice(1).map((x) => x.split(" ").map(Number));

class MinHeap {
  constructor() {
    this.data = [];
  }
  push(value) {
    this.data.push(value);
    let i = this.data.length - 1;
    while (i) {
      const p = (i - 1) >> 1;
      if (this.data[p][0] <= this.data[i][0]) break;
      this.swap(i, p);
      i = p;
    }
  }
  pop() {
    if (this.data.length <= 1) return this.data.pop();
    const root = this.data[0];
    this.data[0] = this.data.pop();
    const n = this.data.length;
    let i = 0;
    while (true) {
      const l = 2 * i + 1;
      const r = 2 * i + 2;
      let s = i;
      if (l < n && this.data[l][0] < this.data[s][0]) s = l;
      if (r < n && this.data[r][0] < this.data[s][0]) s = r;
      if (s === i) break;
      this.swap(i, s);
      i = s;
    }
    return root;
  }
  swap(a, b) {
    [this.data[a], this.data[b]] = [this.data[b], this.data[a]];
  }
  get size() {
    return this.data.length;
  }
}

function solution(N, C) {
  const visited = Array(N).fill(false);
  const pq = new MinHeap();
  pq.push([0, 0]);
  let total = 0;
  let cnt = 0;
  while (pq.size) {
    const [cost, i] = pq.pop();
    if (visited[i]) continue;
    visited[i] = true;
    total += cost;
    cnt++;
    if (cnt === N) break;
    for (let j = 0; j < N; j++) {
      if (!visited[j]) {
        pq.push([C[i][j], j]);
      }
    }
  }
  console.log(total);
}

solution(N, C);
