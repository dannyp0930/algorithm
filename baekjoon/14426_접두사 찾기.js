const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, _M] = input[0].split(" ").map(Number);
const S = input.slice(1, N + 1).sort();
const C = input.slice(N + 1);

function solution(N, S, C) {
  const lowerBound = (target) => {
    let [s, e] = [0, N - 1];
    while (s < e) {
      const m = (s + e) >> 1;
      if (S[m] < target) s = m + 1;
      else e = m;
    }
    return s;
  };
  let answer = 0;
  for (const c of C) {
    const idx = lowerBound(c);
    if (idx < N && S[idx].startsWith(c)) answer++;
  }
  console.log(answer);
}

solution(N, S, C);
