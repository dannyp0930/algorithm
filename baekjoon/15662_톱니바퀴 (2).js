const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const T = Number(input[0]);
const gear = input.slice(1, T + 1);
const K = Number(input[T + 1]);
const command = input.slice(T + 2).map((x) => x.split(" ").map(Number));

function solution(T, gear, K, command) {
  const rotate = (str, dir) => {
    if (dir === 1) return str[7] + str.slice(0, 7);
    return str.slice(1) + str[0];
  };
  const processRotate = (start, dir) => {
    const rotation = Array(T).fill(0);
    rotation[start] = dir;
    let d = dir;
    for (let i = start - 1; i >= 0; i--) {
      if (gear[i][2] !== gear[i + 1][6]) {
        d *= -1;
        rotation[i] = d;
      } else break;
    }
    d = dir;
    for (let i = start + 1; i < T; i++) {
      if (gear[i][6] !== gear[i - 1][2]) {
        d *= -1;
        rotation[i] = d;
      } else break;
    }
    for (let i = 0; i < T; i++) {
      if (rotation[i]) {
        gear[i] = rotate(gear[i], rotation[i]);
      }
    }
  };
  for (const [n, d] of command) {
    processRotate(n - 1, d);
  }
  let answer = 0;
  for (const g of gear) {
    if (g[0] === "1") answer++;
  }
  console.log(answer);
}

solution(T, gear, K, command);
