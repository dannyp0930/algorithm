const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, d, k, c] = input.shift().split(" ").map(Number);
const sushi = input.map(Number);

function solution(N, d, k, c, sushi) {
  for (let i = 0; i < k - 1; i++) sushi.push([sushi[i]]);
  const count = Array(d + 1).fill(0);
  let answer = 0;
  count[c]++;
  let unique = 1;
  for (let i = 0; i < N; i++) {
    if (!i) {
      for (let j = 0; j < k; j++) {
        if (!count[sushi[j]]) unique++;
        count[sushi[j]]++;
      }
    } else {
      count[sushi[i - 1]]--;
      if (!count[sushi[i - 1]]) unique--;
      if (!count[sushi[i + k - 1]]) unique++;
      count[sushi[i + k - 1]]++;
    }
    answer = unique > answer ? unique : answer;
  }
  console.log(answer);
}

solution(N, d, k, c, sushi);
