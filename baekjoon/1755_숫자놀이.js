const fs = require("fs");
const [M, N] = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

function solution(M, N) {
  const numToStr = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];
  const dict = [];
  for (let i = M; i <= N; i++) {
    const name = i
      .toString()
      .split("")
      .map((digit) => numToStr[Number(digit)])
      .join(" ");
    dict.push({ name, num: i });
  }
  dict.sort((a, b) => a.name.localeCompare(b.name));
  let res = "";
  for (let i = 0; i <= N - M; i++) {
    res += dict[i].num;
    if ((i + 1) % 10) res += "\ ";
    else res += "\n";
  }
  console.log(res.trim());
}

solution(M, N);
