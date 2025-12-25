const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, C] = input[0].split(' ').map(Number)
const arr = input[1].split(' ').map(Number)
  
function solution(N, C, arr) {
  const map = new Map()
  for (let i = 0; i < N; i++) {
    const n = arr[i]
    const x = map.get(n)
    if (x) {
      map.set(n, x + 1)
    } else {
      map.set(n, 1)
    }
  }
  const mapToarr = Array.from(map).sort((a, b) => b[1] - a[1])
  const res = []
  for (let [n, cnt] of mapToarr) {
    while (cnt--) {
      res.push(n)
    }
  }
  console.log(res.join(' '))
}

solution(N, C, arr)