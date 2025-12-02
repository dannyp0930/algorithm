const fs = require("fs");
const [A, B] =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split(" ").map(Number)
    : fs.readFileSync("input.txt").toString().trim().split(" ").map(Number);

function solution(A, B) {
  const queue = [4, 7];
  let answer = 0;
  let head = 0;
  while (head < queue.length) {
    const num = queue[head++];
    if (num > B) continue;
    if (num >= A) answer++;
    queue.push(num * 10 + 4);
    queue.push(num * 10 + 7);
  }
  console.log(answer);
}

solution(A, B);
