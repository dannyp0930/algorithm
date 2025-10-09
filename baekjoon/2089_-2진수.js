const fs = require("fs");
const N =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim()
    : fs.readFileSync("input.txt").toString().trim();

function solution() {
  let n = Number(N);
  let answer = "";
  while (n) {
    let r = n % - 2
    n = (n / -2) >> 0;
    if (r < 0) {
      r = 1;
      n++;
    }
    answer = r + answer
  }
  console.log(answer ? answer : '0');
}
solution();
