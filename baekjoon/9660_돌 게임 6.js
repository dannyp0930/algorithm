const fs = require("fs");
const N =
  process.platform === "linux"
    ? Number(fs.readFileSync(0, "utf-8").toString().trim())
    : Number(fs.readFileSync("input.txt").toString().trim());

function solution(N) {
  const r = N % 7;
  if (r === 2 || r === 0) console.log("CY");
  else console.log("SK");
}

solution(N);
