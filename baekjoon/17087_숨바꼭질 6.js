const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution() {
  const [N, S] = input[0].split(" ").map(Number);
  const A = input[1].split(" ").map(Number);
  const diff = new Set();
  for (const a of A) {
    diff.add(a > S ? a - S : S - a);
  }
  const gcd = (a, b) => {
    if (b > a) [a, b] = [b, a];
    while (a % b) {
      [a, b] = [b, a % b];
    }
    return b;
  };
  console.log([...diff].reduce((a, c) => gcd(a, c)));
}

solution();
