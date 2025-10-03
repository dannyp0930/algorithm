const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution() {
  const N = Number(input[0]);
  const M = Number(input[1]);
  const arr = input[2].split(" ").map(Number);
  const frame = new Map();
  for (let i = 0; i < M; i++) {
    const student = arr[i];
    if (frame.has(student)) {
      const item = frame.get(student);
      frame.set(student, { cnt: item.cnt + 1, time: item.time });
    } else {
      if (frame.size === N) {
        const remove = [...frame.entries()].sort((a, b) =>
          a[1].cnt === b[1].cnt ? a[1].time - b[1].time : a[1].cnt - b[1].cnt
        )[0][0];
        frame.delete(remove);
      }
      frame.set(student, { cnt: 1, time: i });
    }
  }
  const answer = [...frame.keys()].sort((a, b) => a - b);
  console.log(answer.join(" "));
}

solution();
