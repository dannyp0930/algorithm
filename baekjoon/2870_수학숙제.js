const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .trim()
  .split("\n");

const N = Number(input[0]);
const homeworks = input.slice(1);

function solution(N, homeworks) {
  const res = [];
  for (let i = 0; i < N; i++) {
    const homework = homeworks[i];
    const nums = homework.match(/\d+/g);
    if (nums) {
      nums.forEach((num) => res.push(BigInt(num)));
    }
  }
  res.sort((a, b) => (a < b ? -1 : a > b ? 1 : 0));
  console.log(res.map((n) => n.toString()).join("\n"));
}

solution(N, homeworks);
