const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim();

function solution(input) {
  const [n, m] = input.split(":").map(Number);
  const GCD = (a, b) => {
    if (a < b) [a, b] = [b, a];
    while (b) {
      [a, b] = [b, a % b];
    }
    return a;
  };
  const gcd = GCD(n, m);
  console.log(`${n / gcd}:${m / gcd}`);
}

solution(input);
