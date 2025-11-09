const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const N = Number(input[0]);
const raw = input[1].split(" ");

function solution(N, raw) {
  const type = Number(raw[0]);
  const fact = Array(N + 1).fill(0n);
  fact[0] = 1n;
  for (let i = 1; i <= N; i++) fact[i] = fact[i - 1] * BigInt(i);
  if (type === 1) {
    let K = BigInt(raw[1]);
    let K0 = K - 1n;
    const nums = Array.from({ length: N }, (_, i) => i + 1);
    const ans = [];
    for (let i = 1; i <= N; i++) {
      const block = fact[N - i];
      const idx = Number(K0 / block);
      ans.push(nums[idx]);
      nums.splice(idx, 1);
      K0 %= block;
    }
    console.log(ans.join(" "));
  } else {
    const seq = raw.slice(1).map(Number);
    const nums = Array.from({ length: N }, (_, i) => i + 1);
    let order0 = 0n;
    for (let i = 0; i < N; i++) {
      const idx = nums.indexOf(seq[i]);
      order0 += BigInt(idx) * fact[N - 1 - i];
      nums.splice(idx, 1);
    }
    console.log((order0 + 1n).toString());
  }
}

solution(N, raw);
