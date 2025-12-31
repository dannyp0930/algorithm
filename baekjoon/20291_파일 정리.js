const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const arr = input.slice(1);

function solution(N, arr) {
  const dic = new Map();
  for (let i = 0; i < N; i++) {
    const [_, ext] = arr[i].split(".");
    const item = dic.get(ext);
    if (item) {
      dic.set(ext, item + 1);
    } else {
      dic.set(ext, 1);
    }
  }
  const res = Array.from(dic).sort((a, b) => (a[0] > b[0] ? 1 : -1));
  console.log(res.map((x) => x.join(" ")).join("\n"));
}

solution(N, arr);
