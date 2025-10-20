const fs = require("fs");
const [L, R] =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split(" ")
    : fs.readFileSync("input.txt").toString().trim().split(" ");

function solution(L, R) {
  if (L.length < R.length) return 0;
  let answer = 0;
  for (let i = 0; i < L.length; i++) {
    if (L[i] === R[i]) {
      if (L[i] === "8") answer++;
    } else break;
  }
  return answer;
}

console.log(solution(L, R));
