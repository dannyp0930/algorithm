const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, M] = input.shift().split(" ").map(Number);
const T = input.map(Number);

function solution(N, M, T) {
  let left = 1n;
  let right = BigInt(Math.max(...T)) * BigInt(M);
  let answer = right;
  while (left <= right) {
    const mid = (left + right) / 2n;
    let people = 0n;
    for (const t of T) {
      people += mid / BigInt(t);
      if (people >= BigInt(M)) break;
    }
    if (people >= BigInt(M)) {
      answer = mid;
      right = mid - 1n;
    } else {
      left = mid + 1n;
    }
  }
  console.log(answer.toString());
}

solution(N, M, T);
