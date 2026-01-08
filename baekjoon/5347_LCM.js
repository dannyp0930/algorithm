const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const n = Number(input[0]);
const test = input.slice(1).map((x) => x.split(" ").map(Number));

function solution(n, test) {
  const GCD = (a, b) => {
    if (a < b) [a, b] = [b, a];
    while (a % b) {
      [a, b] = [b, a % b];
    }
    return b;
  };
  const LCM = (a, b) => (a * b) / GCD(a, b);
  const result = [];
  for (let i = 0; i < n; i++) {
    const [a, b] = test[i];
    result.push(LCM(a, b));
  }
  console.log(result.join("\n"));
}

solution(n, test);
