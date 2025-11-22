const fs = require("fs");
const K =
  process.platform === "linux"
    ? Number(fs.readFileSync(0, "utf-8").toString().trim())
    : Number(fs.readFileSync("input.txt").toString().trim());

function estimateN(K) {
  if (K < 6) return 15;
  const lnK = Math.log(K);
  const lnlnK = Math.log(lnK);
  return Math.floor(K * (lnK + lnlnK));
}

function solution(K) {
  const N = estimateN(500000);
  const eratos = Array(N + 1).fill(true);
  (eratos[0] = false), (eratos[1] = false);
  for (let i = 2; i * i <= N; i++) {
    if (eratos[i]) {
      for (let j = i * i; j <= N; j += i) {
        eratos[j] = false;
      }
    }
  }
  const prime = [];
  for (let i = 2; i <= N; i++) {
    if (eratos[i]) prime.push(i);
  }
  console.log(prime[K - 1]);
}

solution(K);
