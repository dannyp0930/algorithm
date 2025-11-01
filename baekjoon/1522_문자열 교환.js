const fs = require("fs");
const s =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim()
    : fs.readFileSync("input.txt").toString().trim();

function solution(s) {
  const n = s.length;
  const k = s.split("").reduce((a, c) => a + (c === "a" ? 1 : 0), 0);
  if (k === 0 || k === n) return 0;
  let cnt = s
    .slice(0, k)
    .split("")
    .reduce((a, c) => a + (c === "b" ? 1 : 0), 0);
  let answer = cnt;
  for (let i = 1; i < n; i++) {
    if (s[i - 1] === "b") cnt--;
    if (s[(i + k - 1) % n] === "b") cnt++;
    if (answer > cnt) answer = cnt;
  }
  return answer;
}

console.log(solution(s));
