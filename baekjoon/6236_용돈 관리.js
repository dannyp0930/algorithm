const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution() {
  const [N, M] = input.shift().split(" ").map(Number);
  const amount = input.map(Number);
  let lo = Math.max(...amount),
    hi = 1000000000;
  const possible = (k) => {
    let cnt = 0,
      remain = 0;
    for (let i = 0; i < N; i++) {
      if (amount[i] > remain) {
        cnt++;
        remain = k - amount[i];
      } else remain -= amount[i];
    }
    return cnt <= M;
  };
  let answer = 0;
  while (lo <= hi) {
    let mid = (lo + hi) >> 1;
    if (possible(mid)) {
      answer = mid;
      hi = mid - 1;
    } else {
      lo = mid + 1;
    }
  }
  console.log(answer);
}

solution();
