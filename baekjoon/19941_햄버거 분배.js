const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, K] = input[0].split(" ").map(Number);
const H = input[1].split("");

function solution(N, K, H) {
  let answer = 0;
  for (let i = 0; i < N; i++) {
    if (H[i] === "P") {
      const s = i < K ? 0 : i - K;
      const e = i + K >= N ? N - 1 : i + K;
      for (j = s; j <= e; j++) {
        if (H[j] === "H") {
          H[j] = "E";
          answer++;
          break;
        }
      }
    }
  }
  console.log(answer);
}

solution(N, K, H);
