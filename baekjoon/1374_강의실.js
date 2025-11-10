const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input.shift());
const lecture = input.map((x) => x.split(" ").map(Number));

class MinHeap {
  constructor() {
    this.data = [];
  }
  get size() {
    return this.data.length;
  }
  push(value) {
    this.data.push(value);
    let i = this.data.length - 1;
    while (i) {
      const p = (i - 1) >> 1;
      if (this.data[i][2] < this.data[p][2]) {
        this._swap(i, p);
        i = p;
      } else break;
    }
  }
  pop() {
    if (!this.data.length) return undefined;
    const root = this.data[0];
    const last = this.data.pop();
    if (this.data.length) {
      this.data[0] = last;
      const n = this.data.length;
      let i = 0;
      while (true) {
        const l = 2 * i + 1;
        const r = 2 * i + 2;
        let s = i;
        if (l < n && this.data[l][2] < this.data[s][2]) s = l;
        if (r < n && this.data[r][2] < this.data[s][2]) s = r;
        if (s === i) break;
        this._swap(i, s);
        i = s;
      }
    }
    return root;
  }
  _swap(a, b) {
    [this.data[a], this.data[b]] = [this.data[b], this.data[a]];
  }
}

function solution(N, lecture) {
  lecture.sort((a, b) => a[1] - b[1]);
  const heap = new MinHeap();
  heap.push(lecture[0]);
  for (let i = 1; i < N; i++) {
    if (heap.data[0][2] <= lecture[i][1]) heap.pop();
    heap.push(lecture[i]);
  }
  console.log(heap.size);
}

solution(N, lecture);
