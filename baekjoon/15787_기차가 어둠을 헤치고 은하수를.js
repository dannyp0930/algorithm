const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const commands = input.slice(1).map((x) => x.split(" ").map(Number));

function solution() {
  const trains = Array(N).fill(0);
  const C1 = (i, x) => (trains[i - 1] |= 1 << (x - 1));
  const C2 = (i, x) => (trains[i - 1] &= ~(1 << (x - 1)));
  const C3 = (i) => (trains[i - 1] = (trains[i - 1] << 1) & ((1 << 20) - 1));
  const C4 = (i) => (trains[i - 1] >>= 1);
  for (const c of commands) {
    switch (c[0]) {
      case 1:
        C1(c[1], c[2]);
        break;
      case 2:
        C2(c[1], c[2]);
        break;
      case 3:
        C3(c[1]);
        break;
      case 4:
        C4(c[1]);
        break;
    }
  }
  console.log(new Set(trains).size);
}

solution();
