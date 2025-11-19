const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [M, N, L] = input[0].split(" ").map(Number);
const xPos = input[1].split(" ").map(Number);
const animals = input.slice(2, N + 2).map((x) => x.split(" ").map(Number));

function solution(M, N, L, xPos, animals) {
  let answer = 0;
  xPos.sort((a, b) => a - b);
  for (let i = 0; i < N; i++) {
    const [a, b] = animals[i];
    if (b > L) continue;
    const [left, right] = [a - L + b, a + L - b];
    let [lo, hi] = [0, M];
    while (lo < hi) {
      const mid = (lo + hi) >> 1;
      if (xPos[mid] < left) lo = mid + 1;
      else hi = mid;
    }
    if (lo < M && xPos[lo] <= right) answer++;
  }
  console.log(answer);
}

solution(M, N, L, xPos, animals);
