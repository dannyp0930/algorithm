const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution() {
  input.shift();
  const arr = input.map(Number);
  const stack = [];
  let answer = 0;
  for (const h of arr) {
    while (stack.length && stack[stack.length - 1] <= h) {
      stack.pop();
    }
    answer += stack.length;
    stack.push(h);
  }
  console.log(answer);
}

solution();
