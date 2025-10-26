const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const balls = input[1].split("");

function solution() {
  const red = balls.filter((a) => a === "R").length;
  const blue = N - red;
  let answer = Math.min(red, blue);
  let cnt = 0;
  for (let i = 0; i < N; i++) {
    if (balls[i] !== balls[0]) break;
    cnt++;
  }
  answer =
    balls[0] === "R"
      ? Math.min(answer, red - cnt)
      : Math.min(answer, blue - cnt);
  cnt = 0;
  for (let i = N - 1; i >= 0; i--) {
    if (balls[i] !== balls[N - 1]) break;
    cnt++;
  }
  answer =
    balls[N - 1] === "R"
      ? Math.min(answer, red - cnt)
      : Math.min(answer, blue - cnt);
  console.log(answer);
}

solution(N, balls);
