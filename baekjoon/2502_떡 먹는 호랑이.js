const fs = require("fs");
const [D, K] =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split(" ").map(Number)
    : fs.readFileSync("input.txt").toString().trim().split(" ").map(Number);

function solution() {
  const dpA = Array(D).fill(0);
  const dpB = Array(D).fill(0);
  dpA[0] = 1;
  dpB[1] = 1;
  for (let i = 2; i < D; i++) {
    dpA[i] = dpA[i - 1] + dpA[i - 2];
    dpB[i] = dpB[i - 1] + dpB[i - 2];
  }
  let a = 1;
  while ((K - a * dpA[D - 1]) % dpB[D - 1]) {
    a++;
  }
  console.log(a);
  console.log((K - a * dpA[D - 1]) / dpB[D - 1]);
}

solution();
