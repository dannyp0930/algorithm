const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution() {
  const [M, N] = input[0].split(" ").map(Number);
  const L = input[1].split(" ").map(Number);
  let s = 1;
  let e = 1000000000;
  let answer = 0;
  while (s <= e) {
    let mid = (s + e) >> 1;
    let cnt = 0;
    for (const l of L) {
      cnt += (l / mid) >> 0;
    }
    if (cnt >= M) {
      s = mid + 1;
      answer = mid;
    } else e = mid - 1;
  }
  console.log(answer);
}

solution();
