const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input[0].split(" ").map(Number);
const titles = [];
const limits = [];
for (let i = 1; i <= N; i++) {
  const [title, limit] = input[i].split(" ");
  titles.push(title);
  limits.push(Number(limit));
}
const powers = input.slice(N + 1).map(Number);

function solution(N, M, titles, limits, powers) {
  const res = [];
  for (let i = 0; i < M; i++) {
    const power = powers[i];
    let [l, r] = [0, N - 1];
    let idx = 0;
    while (l <= r) {
      const m = (l + r) >> 1;
      if (power <= limits[m]) {
        idx = m;
        r = m - 1;
      } else {
        l = m + 1;
      }
    }
    res.push(titles[idx]);
  }
  console.log(res.join("\n"));
}

solution(N, M, titles, limits, powers);
