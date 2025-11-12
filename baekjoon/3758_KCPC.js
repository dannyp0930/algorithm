const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution(n, k, t, m) {
  const info = Array.from({ length: n }, (_, i) => ({
    id: i + 1,
    scores: Array(k).fill(0),
    total: 0,
    cnt: 0,
    last: 0,
  }));
  for (let idx = 0; idx < m; idx++) {
    const [i, j, s] = input[pos++].split(" ").map(Number);
    const team = info[i - 1];
    if (team.scores[j - 1] < s) {
      team.total += s - team.scores[j - 1];
      team.scores[j - 1] = s;
    }
    team.cnt++;
    team.last = idx;
  }
  info.sort((a, b) => b.total - a.total || a.cnt - b.cnt || a.last - b.last);
  return info.findIndex((x) => x.id === t) + 1;
}

let T = Number(input[0]);
let pos = 1;
const result = [];
while (T--) {
  const [n, k, t, m] = input[pos++].split(" ").map(Number);
  result.push(solution(n, k, t, m));
}
console.log(result.join("\n"));
