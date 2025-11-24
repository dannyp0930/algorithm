const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, K] = input[0].split(" ").map(Number);
const pots = input.slice(1).map(Number);

function solution(N, K, pots) {
  let [s, e] = [1, Math.max(...pots)];
  let answer = 0;
  while (s <= e) {
    const mid = Math.floor((s + e) / 2);
    let cnt = 0;
    for (const pot of pots) {
      cnt += Math.floor(pot / mid);
    }
    if (cnt >= K) {
      answer = mid;
      s = mid + 1;
    } else {
      e = mid - 1;
    }
  }
  console.log(answer);
}

solution(N, K, pots);
