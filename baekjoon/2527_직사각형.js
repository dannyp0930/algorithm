const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs
        .readFileSync(0, "utf-8")
        .toString()
        .trim()
        .split("\n")
        .map((x) => x.split(" ").map(Number))
    : fs
        .readFileSync("input.txt")
        .toString()
        .trim()
        .split("\n")
        .map((x) => x.split(" ").map(Number));

function solution(input) {
  for (const [x1, y1, x2, y2, x3, y3, x4, y4] of input) {
    if (x1 > x4 || x2 < x3 || y1 > y4 || y2 < y3) {
      console.log("d");
    } else if ((x1 === x4 || x2 === x3) && (y1 === y4 || y2 === y3)) {
      console.log("c");
    } else if ((x1 === x4 || x2 === x3 || y1 === y4 || y2 === y3)) {
      console.log("b");
    } else {
      console.log("a");
    }
  }
}

solution(input);
