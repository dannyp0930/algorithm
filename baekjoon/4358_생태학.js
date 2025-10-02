const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution() {
  const N = input.length;
  const dict = new Map();
  for (const tree of input) {
    if (dict.has(tree)) {
      dict.set(tree, dict.get(tree) + 1);
    } else {
      dict.set(tree, 1);
    }
  }
  const arr = Array.from(dict)
    .sort()
    .map((a) => [a[0], ((a[1] / N) * 100).toFixed(4)].join(" "));
  console.log(arr.join("\n"));
}

solution();
