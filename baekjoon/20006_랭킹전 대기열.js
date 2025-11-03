const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

const [p, m] = input.shift().split(" ").map(Number);
const players = input.map((x) => x.split(" "));

function solution(p, m, players) {
  const rooms = [];
  for (const player of players) {
    const [l, n] = [Number(player[0]), player[1]];
    let flag = true;
    for (let i = 0; i < rooms.length; i++) {
      if (
        rooms[i].length < m &&
        rooms[i][0][0] - 10 <= l &&
        l <= rooms[i][0][0] + 10
      ) {
        rooms[i].push([l, n]);
        flag = false;
        break;
      }
    }
    if (flag) rooms.push([[l, n]]);
  }
  for (const room of rooms) {
    if (room.length === m) console.log("Started!");
    else console.log("Waiting!");
    console.log(
      room
        .sort((a, b) => (a[1] > b[1] ? 1 : -1))
        .map((x) => x.join(" "))
        .join("\n")
    );
  }
}

solution(p, m, players);
