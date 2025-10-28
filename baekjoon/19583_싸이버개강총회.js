const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function dateToNum(date) {
  const [h, m] = date.split(":").map(Number);
  return h * 60 + m;
}

const [S, E, Q] = input.shift().split(" ").map(dateToNum);
const chats = input.map((x) => {
  const y = x.split(" ");
  y[0] = dateToNum(y[0]);
  return y;
});

function solution(S, E, Q, chats) {
  const enter = new Set();
  const attend = new Set();
  for (const [time, name] of chats) {
    if (time <= S) enter.add(name);
    else if (E <= time && time <= Q && enter.has(name)) attend.add(name);
  }
  console.log(attend.size);
}

solution(S, E, Q, chats);
