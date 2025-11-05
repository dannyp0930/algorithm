const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, K] = input[0].split(" ").map(Number);
const dolls = input[1].split(" ").map(Number);

function solution(N, K, dolls) {
  let l = 0;
  let cnt = 0;
  let answer = N + 1;
  for (let r = 0; r < N; r++) {
    if (dolls[r] === 1) cnt++;
    while (cnt >= K) {
      answer = Math.min(answer, r - l + 1);
      if (dolls[l] === 1) cnt--;
      l++;
    }
  }
  console.log(answer > N ? -1 : answer);
}

solution(N, K, dolls);
