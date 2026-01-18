const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim()
  .split("\n");

function solution(input) {
  const N = Number(input[0]);
  const arr = input.slice(1).map((x) => x.split(" ").map(Number));
  const comb = (cards) => {
    let res = 0;
    const backtrack = (s, cur, cnt) => {
      if (cnt === 3) {
        const units = cur % 10;
        if (res < units) res = units;
        return;
      }
      for (let i = s; i < 5; i++) {
        backtrack(i + 1, cur + cards[i], cnt + 1);
      }
    };
    backtrack(0, 0, 0);
    return res;
  };
  let max = 0;
  let answer = 0;
  for (let i = 0; i < N; i++) {
    const cards = arr[i];
    const res = comb(cards);
    if (max <= res) {
      max = res;
      answer = i + 1;
    }
  }
  console.log(answer);
}

solution(input);
