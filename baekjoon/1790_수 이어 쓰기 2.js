const fs = require("fs");
const [N, k] =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split(" ").map(Number)
    : fs.readFileSync("input.txt").toString().trim().split(" ").map(Number);

function solution(N, k) {
  let i = 1;
  while (true) {
    let cnt = 9 * 10 ** (i - 1) * i;
    if (k > cnt) k -= cnt;
    else break;
    i++;
  }
  const nIdx = ((k - 1) / i) >> 0;
  const target = 10 ** (i - 1) + nIdx;
  if (target > N) console.log(-1);
  else {
    const cIdx = (k - 1) % i;
    console.log(target.toString()[cIdx]);
  }
}

solution(N, k);
