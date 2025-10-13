const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");
const [N, P] = input.shift().split(" ").map(Number);
const melodies = input.map((x) => x.split(" ").map(Number));

function solution(N, P, melodies) {
    let answer = 0;
    const stack = Array.from(Array(P + 1), () => []);
    for (const [idx, fret] of melodies) {
        while (stack[idx].length && stack[idx][stack[idx].length - 1] > fret) {
            stack[idx].pop();
            answer++;
        }
        if (!stack[idx].length || stack[idx][stack[idx].length - 1] < fret) {
            stack[idx].push(fret)
            answer++;
        }
    }

    return answer
}

console.log(solution(N, P, melodies));
