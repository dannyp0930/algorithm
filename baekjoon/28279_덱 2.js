const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

class Deque {
  constructor() {
    this.items = {};
    this.first = 0;
    this.last = 0;
  }
  push(item) {
    this.items[this.last++] = item;
  }
  unshift(item) {
    this.items[--this.first] = item;
  }
  pop() {
    if (this.isEmpty()) return undefined;
    const item = this.items[--this.last];
    delete this.items[this.last];
    return item;
  }
  shift() {
    if (this.isEmpty()) return undefined;
    const item = this.items[this.first];
    delete this.items[this.first++];
    return item;
  }
  peekFirst() {
    if (this.isEmpty()) return undefined;
    return this.items[this.first];
  }
  peekLast() {
    if (this.isEmpty()) return undefined;
    return this.items[this.last - 1];
  }
  size() {
    return this.last - this.first;
  }
  isEmpty() {
    return this.first === this.last;
  }
}

function solution(input) {
  const N = Number(input[0]);
  const deque = new Deque();
  const res = [];
  for (let i = 1; i <= N; i++) {
    const line = input[i].split(" ");
    const q = Number(line[0]);
    switch (q) {
      case 1:
        deque.unshift(Number(line[1]));
        break;
      case 2:
        deque.push(Number(line[1]));
        break;
      case 3:
        res.push(deque.shift() ?? -1);
        break;
      case 4:
        res.push(deque.pop() ?? -1);
        break;
      case 5:
        res.push(deque.size());
        break;
      case 6:
        res.push(deque.isEmpty() ? 1 : 0);
        break;
      case 7:
        res.push(deque.peekFirst() ?? -1);
        break;
      case 8:
        res.push(deque.peekLast() ?? -1);
        break;
    }
  }
  console.log(res.join("\n"));
}

solution(input);
