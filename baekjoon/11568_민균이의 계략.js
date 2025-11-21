const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const cards = input[1].split(" ").map(Number);

function lis(N, cards) {
  const dp = Array(N).fill(0);
  for (let i = 0; i < N; i++) {
    dp[i] = 1;
    for (let j = 0; j < i; j++) {
      if (cards[i] > cards[j]) {
        dp[i] = Math.max(dp[i], dp[j] + 1);
      }
    }
  }
  console.log(Math.max(...dp));
}

function lisBinarySearch(N, cards) {
  const lis = [];
  for (let i = 0; i < N; i++) {
    let [s, e] = [0, lis.length];
    while (s < e) {
      const mid = (s + e) >> 1;
      if (cards[i] > lis[mid]) s = mid + 1;
      else e = mid;
    }
    lis[e] = cards[i];
  }
  console.log(lis.length);
}

lis(N, cards);
lisBinarySearch(N, cards);
