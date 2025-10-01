const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const T = Number(input.shift());

function solution() {
  for (let i = 0; i < T; i++) {
    const N = Number(input[i * 2]);
    const arr = input[i * 2 + 1].split(" ").map(Number);
    let max = 0;
    let profit = 0;
    for (let j = N - 1; j >= 0; j--) {
      if (max < arr[j]) {
        max = arr[j];
      } else {
        profit += max - arr[j];
      }
    }
    console.log(profit);
  }
}

solution();
