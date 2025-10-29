const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution(input) {
  const N = input.length;
  for (let i = 0; i < N - 1; i++) {
    const S = input[i];
    const stack = [];
    let res = 0;
    for (const ch of S) {
      if (ch === "{") {
        stack.push("{");
      } else {
        if (stack[stack.length - 1] === "{") {
          stack.pop();
        } else {
          res++;
          stack.push("{");
        }
      }
    }
    res += stack.length / 2;
    console.log(`${i + 1}. ${res}`);
  }
}

solution(input);
