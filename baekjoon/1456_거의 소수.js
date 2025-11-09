const fs = require("fs");
const [A, B] =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split(" ").map(Number)
    : fs.readFileSync("input.txt").toString().trim().split(" ").map(Number);

function solution(A, B) {
  const b = (B ** (1 / 2)) >> 0;
  const isPrime = Array(b + 1).fill(true);
  isPrime[0] = false;
  isPrime[1] = false;
  for (let i = 2; i * i <= b; i++) {
    if (!isPrime[i]) continue;
    for (let j = 2 * i; j <= b; j += i) {
      isPrime[j] = false;
    }
  }
  let answer = 0;
  for (let p = 2; p <= b; p++) {
    if (!isPrime[p]) continue;
    let power = p ** 2;
    while (power <= B) {
      if (power >= A) answer++;
      if (power * p > B) break;
      power *= p;
    }
  }
  console.log(answer);
}

solution(A, B);
