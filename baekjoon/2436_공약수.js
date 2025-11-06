const fs = require("fs");
const [a, b] =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split(" ").map(Number)
    : fs.readFileSync("input.txt").toString().trim().split(" ").map(Number);

function solution(a, b) {
  const gcd = (a, b) => {
    if (a < b) [a, b] = [b, a];
    while (b) {
      [a, b] = [b, a % b];
    }
    return a;
  };
  const n = b / a;
  for (let i = parseInt(n ** (1 / 2)); i > 0; i--) {
    if (n % i === 0) {
      const j = n / i;
      if (gcd(i, j) === 1) {
        console.log(a * i, a * j);
        return;
      }
    }
  }
}

solution(a, b);
