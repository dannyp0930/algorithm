const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");
const [C, R] = input.shift().split(" ").map(Number);
const N = Number(input.shift());
const pos = input.pop().split(" ").map(Number);
const shops = input.map((x) => x.split(" ").map(Number));

function solution(C, R, N, shops, pos) {
  let answer = 0;
  const getPos = (dir, dist) => {
    if (dir === 1) {
      return dist;
    } else if (dir === 2) {
      return 2 * C + R - dist;
    } else if (dir === 3) {
      return 2 * (R + C) - dist;
    } else {
      return C + dist;
    }
  };
  const perimeter = 2 * (R + C);
  const xPos = getPos(...pos);
  for (const shop of shops) {
    const shopPos = getPos(...shop);
    const diff = xPos > shopPos ? xPos - shopPos : shopPos - xPos;
    answer += perimeter < 2 * diff ? perimeter - diff : diff;
  }
  return answer;
}

console.log(solution(C, R, N, shops, pos));
