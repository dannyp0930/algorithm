const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const cur = input[1].split("").map(Number).map(Boolean);
const target = input[2].split("").map(Number).map(Boolean);

function solution(N, cur, target) {
  const simulate = (cur, target, cnt) => {
    if (cnt) {
      cur[0] = !cur[0];
      cur[1] = !cur[1];
    }
    for (let i = 1; i < N; i++) {
      if (cur[i - 1] !== target[i - 1]) {
        cnt++;
        cur[i - 1] = !cur[i - 1];
        cur[i] = !cur[i];
        if (i < N - 1) cur[i + 1] = !cur[i + 1];
      }
    }
    for (let i = 0; i < N; i++) {
      if (cur[i] !== target[i]) return Infinity;
    }
    return cnt;
  };
  const res1 = simulate([...cur], target, 0);
  const res2 = simulate([...cur], target, 1);
  const res = res1 < res2 ? res1 : res2;
  return res === Infinity ? -1 : res;
}

console.log(solution(N, cur, target));
