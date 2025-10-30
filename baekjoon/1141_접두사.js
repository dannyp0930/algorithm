const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input.shift());
const words = input;

function solution(N, words) {
  words.sort();
  let answer = N;
  for (let i = 0; i < N - 1; i++) {
    for (let j = i + 1; j < N; j++) {
      if (words[j].startsWith(words[i])) {
        answer--;
        break;
      }
    }
  }
  console.log(answer);
}

solution(N, words);
