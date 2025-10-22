const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const T = Number(input.shift());

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
    if (!this.data.length) undefined;
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
      if (this.data[i] < this.data[p]) {
        this._swap(i, p);
        i = p;
      } else break;
    }
  }
  _siftDown() {
    const n = this.data.length;
    let i = 0;
    while (true) {
      const l = i * 2 + 1;
      const r = i * 2 + 2;
      let s = i;
      if (l < n && this.data[l] < this.data[s]) s = l;
      if (r < n && this.data[r] < this.data[s]) s = r;
      if (s === i) break;
      this._swap(i, s);
      i = s;
    }
  }
  _swap(a, b) {
    [this.data[a], this.data[b]] = [this.data[b], this.data[a]];
  }
}
function solution(T, input) {
  let i = 0;
  while (i < T) {
    const C = input[i * 2 + 1].split(" ").map(Number);
    const heap = new MinHeap();
    for (const c of C) {
      heap.push(c);
    }
    let answer = 0;
    while (heap.size) {
      const a = heap.pop();
      const b = heap.pop();
      const tmp = a + b;
      answer += tmp;
      if (heap.size) {
        heap.push(tmp);
      }
    }
    console.log(answer);
    i++;
  }
}

solution(T, input);
