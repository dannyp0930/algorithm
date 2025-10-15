const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = +input[0];
const arr = input[1].split(" ").map(Number);

function solution() {
  const tails = [arr[0]];
  for (const num of arr) {
    if (!tails.length || num < tails[tails.length - 1]) {
      tails.push(num);
    } else {
      let l = 0,
        r = tails.length - 1;
      let ans = 0;
      while (l <= r) {
        const mid = (l + r) >> 1;
        if (tails[mid] < num) {
          ans = mid;
          r = mid - 1;
        } else {
          l = mid + 1;
        }
      }
      tails[ans] = num;
    }
  }
  console.log(N - tails.length);
}

solution();
