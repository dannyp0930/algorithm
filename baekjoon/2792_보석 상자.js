const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, M] = input.shift().split(" ").map(Number);
const marbles = [0, ...input.map(Number)];

function solution(N, marbles) {
  const MAX = Math.max(...marbles);
  let l = 1;
  let r = MAX;
  let answer = 0;
  while (l <= r) {
    const mid = (l + r) >> 1;
    let cnt = 0;
    for (const marble of marbles) {
      cnt += ((marble / mid) >> 0) + (marble % mid ? 1 : 0);
    }
    if (cnt <= N) {
      answer = mid;
      r = mid - 1;
    } else {
      l = mid + 1;
    }
  }
  console.log(answer);
}

solution(N, marbles);
