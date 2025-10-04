const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution() {
  const [N, K] = input[0].split(" ").map(Number);
  const arr = input[1].split(" ").map(Number);
  let s = 0, e = 0;
  let answer = 0;
  const sequence = {};
  while (s <= e && e < N) {
    while (sequence[arr[e]] === K) {
      sequence[arr[s]]--;
      s++;
    }
    answer = answer < e - s + 1 ? e - s + 1 : answer;
    if (sequence[arr[e]]) sequence[arr[e]] += 1;
    else sequence[arr[e]] = 1;
    e++;
  }
  console.log(answer);
}

solution();