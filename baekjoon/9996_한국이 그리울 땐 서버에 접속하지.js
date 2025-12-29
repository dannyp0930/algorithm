const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const pattern = input[1];
const files = input.slice(2);

function solution(N, pattern, files) {
  const res = [];
  const [pre, suf] = pattern.split("*");
  const match = (file) => {
    const fileLen = file.length;
    const preLen = pre.length;
    const sufLen = suf.length;
    if (fileLen < preLen + sufLen) return "NE";
    if (file.startsWith(pre) && file.endsWith(suf)) return "DA";
    return "NE";
  };
  for (let i = 0; i < N; i++) {
    const file = files[i];
    res.push(match(file));
  }
  console.log(res.join("\n"));
}

solution(N, pattern, files);
