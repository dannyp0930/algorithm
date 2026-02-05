const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim()
  .split("\n");

function solution(input) {
  const N = Number(input[0]);
  const students = [];
  for (let i = 1; i <= N; i++) {
    const [country, id, score] = input[i].split(" ").map(Number);
    students.push({ country, id, score });
  }
  students.sort((a, b) => b.score - a.score);
  const countryMedal = {};
  const result = [];
  for (const student of students) {
    if (result.length === 3) break;
    const { country, id } = student;
    if (!countryMedal[country] || countryMedal[country] < 2) {
      result.push(`${country} ${id}`);
      countryMedal[country] = (countryMedal[country] || 0) + 1;
    }
  }
  console.log(result.join("\n"));
}

solution(input);
