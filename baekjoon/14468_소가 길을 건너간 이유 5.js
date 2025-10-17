const fs = require("fs");
const string =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim()
    : fs.readFileSync("input.txt").toString().trim();

function solution(string) {
  let answer = 0;
  const routes = Array.from({ length: 26 }, () => []);
  for (let i = 0; i < 52; i++) {
    const charIdx = string[i].charCodeAt() - 65;
    routes[charIdx].push(i);
  }
  for (let i = 0; i < 26; i++) {
    for (let j = 0; j < 26; j++) {
      if (
        routes[i][0] < routes[j][0] &&
        routes[j][0] < routes[i][1] &&
        routes[i][1] < routes[j][1]
      ) {
        answer++;
      }
    }
  }
  console.log(answer);
}

solution(string);
