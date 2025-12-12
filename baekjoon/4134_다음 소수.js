const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n").map(Number)
    : fs.readFileSync("input.txt").toString().trim().split("\n").map(Number);

function solution(input) {
  const isPrime = (n) => {
    if (n <= 1) return false;
    if (n === 2) return true;
    if (n % 2 === 0) return false;
    for (let i = 3; i * i <= n; i += 2) {
      if (n % i === 0) return false;
    }
    return true;
  };
  const T = input[0];
  const res = [];
  for (let i = 1; i <= T; i++) {
    let n = input[i];
    if (n <= 2) {
      res.push(2);
      continue;
    }
    while (!isPrime(n)) {
      n++;
    }
    res.push(n);
  }
  console.log(res.join("\n"));
}

solution(input);
