const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const query = input.slice(1).map((x) => x.split(" ").map(Number));

function solution(N, query) {
  const stack = [];
  const res = [];
  for (const [c, v] of query) {
    if (c === 1) stack.push(v);
    else if (c === 2) res.push(stack.pop() ?? -1);
    else if (c === 3) res.push(stack.length);
    else if (c === 4) res.push(stack.length ? 0 : 1);
    else res.push(stack[stack.length - 1] ?? -1);
  }
  console.log(res.join("\n"));
}

solution(N, query);
