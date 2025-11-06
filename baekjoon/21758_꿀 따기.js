const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const honey = input[1].split(" ").map(Number);

function solution(N, honey) {
  const prefix = Array(N).fill(0);
  for (let i = 0; i < N; i++) {
    prefix[i] = (i ? prefix[i - 1] : 0) + honey[i];
  }
  const total = prefix[N - 1];
  let answer = 0;
  for (let i = 1; i < N - 1; i++) {
    const sum = total - honey[0] - honey[i] + (total - prefix[i]);
    answer = sum > answer ? sum : answer;
  }
  for (let i = 1; i < N - 1; i++) {
    const sum = total - honey[N - 1] - honey[i] + prefix[i - 1];
    answer = sum > answer ? sum : answer;
  }
  for (let i = 1; i < N - 1; i++) {
    const sum = (prefix[i] - honey[0]) + (total - prefix[i - 1] - honey[N - 1]);
    answer = sum > answer ? sum : answer;
  }
  console.log(answer);
}

solution(N, honey);
