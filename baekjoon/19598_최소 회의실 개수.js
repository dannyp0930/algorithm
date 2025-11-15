const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

class MinHeap {
  constructor() {
    this.items = [];
  }
  get size() {
    return this.items.length;
  }
  push(value) {
    this.items.push(value);
    let i = this.items.length - 1;
    while (i) {
      const p = (i - 1) >> 1;
      if (this.items[i][1] < this.items[p][1]) {
        this._swap(i, p);
        i = p;
      } else break;
    }
  }
  pop() {
    if (!this.items.length) return undefined;
    const root = this.items[0];
    const last = this.items.pop();
    if (this.items.length) {
      this.items[0] = last;
      const n = this.items.length;
      let i = 0;
      while (true) {
        const l = i * 2 + 1;
        const r = i * 2 + 2;
        let s = i;
        if (l < n && this.items[l][1] < this.items[s][1]) s = l;
        if (r < n && this.items[r][1] < this.items[s][1]) s = r;
        if (s === i) break;
        this._swap(i, s);
        i = s;
      }
    }
    return root;
  }
  _swap(a, b) {
    [this.items[a], this.items[b]] = [this.items[b], this.items[a]];
  }
}

const N = Number(input.shift());
const meetings = input.map((x) => x.split(" ").map(Number));

function solution(N, meetings) {
  meetings.sort((a, b) => a[0] - b[0]);
  const heap = new MinHeap();
  heap.push(meetings[0]);
  for (let i = 1; i < N; i++) {
    if (heap.items[0][1] <= meetings[i][0]) heap.pop();
    heap.push(meetings[i]);
  }
  console.log(heap.size);
}

solution(N, meetings);
