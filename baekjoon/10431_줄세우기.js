const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution(input) {
  const P = Number(input[0]);
  const res = [];
  for (let i = 1; i <= P; i++) {
    const [t, ...heights] = input[i].split(" ").map(Number);
    let steps = 0;
    const line = [];
    for (const h of heights) {
      for (const l of line) {
        if (l > h) steps++;
      }
      line.push(h);
      line.sort((a, b) => a - b);
    }
    res.push([t, steps]);
  }
  console.log(res.map((x) => x.join(" ")).join("\n"));
}

solution(input);
