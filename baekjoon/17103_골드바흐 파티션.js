const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n").map(Number)
    : fs.readFileSync("input.txt").toString().trim().split("\n").map(Number);
input.shift();
function solution() {
  const n = 1000000;
  const eratos = Array(n + 1).fill(true);
  (eratos[0] = false), (eratos[1] = false);
  const m = (n ** 0.5) >> 0;
  for (let i = 2; i <= m + 1; i++) {
    if (eratos[i]) {
      for (let j = i + i; j <= n; j += i) {
        eratos[j] = false;
      }
    }
  }
  for (const c of input) {
    let cnt = 0;
    for (let i = 2; i <= c >> 1; i++) {
        if (eratos[i] && eratos[c - i]) cnt++;
    }
    console.log(cnt);
  }
}

solution();
