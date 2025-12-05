const fs = require("fs");
const K = BigInt(
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim()
    : fs.readFileSync("input.txt").toString().trim()
);

function solution(K) {
  let len = 1n;
  let cnt = 2n;
  let acc = 2n;
  while (acc < K) {
    len++;
    cnt *= 2n;
    acc += cnt;
  }
  const idx = K - (acc - cnt) - 1n;
  const b = idx.toString(2).padStart(Number(len), "0");
  let s = "";
  for (let c of b) s += c === "0" ? "4" : "7";
  console.log(s);
}

solution(K);
