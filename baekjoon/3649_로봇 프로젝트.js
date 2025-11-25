const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let stage = 0;
let x = 0;
let n = 0;
let l = [];
let cnt = 0;

rl.on("line", (line) => {
  if (line.trim() === "") return;
  if (stage === 0) {
    x = Number(line) * 10000000;
    stage = 1;
  } else if (stage === 1) {
    n = Number(line);
    l = new Array(n);
    cnt = 0;
    if (n === 0) {
      solution(x, n, l);
      stage = 0;
    } else {
      stage = 2;
    }
  } else {
    l[cnt++] = Number(line);
    if (cnt === n) {
      l.sort((a, b) => a - b);
      solution(x, n, l);
      stage = 0;
    }
  }
});

function solution(x, n, l) {
  let [s, e] = [0, n - 1];
  while (s < e) {
    const sum = l[s] + l[e];
    if (sum === x) {
      return console.log(`yes ${l[s]} ${l[e]}`);
    } else if (sum < x) s++;
    else e--;
  }
  return console.log("danger");
}
