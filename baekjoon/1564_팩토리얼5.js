const fs = require("fs");
const N = Number(
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim()
    : fs.readFileSync("input.txt").toString().trim()
);

function solution(N) {
  let res = 1;
  let cnt2 = 0;
  let cnt5 = 0;
  for (let i = 1; i <= N; i++) {
    let x = i;
    while (x % 2 === 0) {
      x /= 2;
      cnt2++;
    }
    while (x % 5 === 0) {
      x /= 5;
      cnt5++;
    }
    res = (res * x) % 100000;
  }
  for (let i = 0; i < cnt2 - cnt5; i++) {
    res = (res * 2) % 100000;
  }
  console.log(res.toString().padStart(5, "0"));
}

solution(N);
