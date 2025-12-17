const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution(input) {
  const N = Number(input[0]);
  const dance = new Set(["ChongChong"]);
  for (let i = 1; i <= N; i++) {
    const [A, B] = input[i].split(" ");
    if (dance.has(A) || dance.has(B)) {
      dance.add(A)
      dance.add(B)
    }
  }
  console.log(dance.size)
}

solution(input);
