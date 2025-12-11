const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const arr = input[1].split(" ").map(Number);

function solution(N, arr) {
  const stack = [];
  let order = 1;
  for (let i = 0; i < N; i++) {
    if (order !== arr[i]) stack.push(arr[i]);
    else order++;
    while (stack.length && stack[stack.length - 1] === order) {
      stack.pop();
      order++;
    }
  }
  console.log(order === N + 1 ? "Nice" : "Sad");
}

solution(N, arr);
