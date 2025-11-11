const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution(input) {
  const T = input[0];
  for (let t = 0; t < T; t++) {
    const [W, K] = [input[t * 2 + 1], Number(input[t * 2 + 2])];
    const pos = Array.from({ length: 26 }, () => []);
    for (let i = 0; i < W.length; i++) {
      pos[W.charCodeAt(i) - 97].push(i);
    }
    let min = 10000;
    let max = 0;
    for (let i = 0; i < 26; i++) {
      const idx = pos[i];
      if (idx.length < K) continue;
      for (let j = 0; j <= idx.length - K; j++) {
        const len = idx[j + K - 1] - idx[j] + 1;
        if (min > len) min = len;
        if (max < len) max = len;
      }
    }
    console.log(max === 0 ? -1 : `${min} ${max}`);
  }
}

solution(input);
