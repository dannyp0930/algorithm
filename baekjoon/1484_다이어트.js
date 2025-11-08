const fs = require("fs");
const G =
  process.platform === "linux"
    ? Number(fs.readFileSync(0, "utf-8").toString().trim())
    : Number(fs.readFileSync("input.txt").toString().trim());

function solution(G) {
  let l = 1;
  let r = 2;
  const res = [];
  while (l < r) {
    const diff = r ** 2 - l ** 2;
    if (diff === G) {
      res.push(r);
      l++;
      r++;
    } else if (diff > G) {
      l++;
    } else {
      r++;
    }
  }
  console.log(res.length ? res.join("\n") : -1);
}

solution(G);
