const fs = require("fs");
const input =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim().split("\n")
    : fs.readFileSync("input.txt").toString().trim().split("\n");

function solution() {
  const [S, P] = input[0].split(" ").map(Number);
  const string = input[1];
  const [A, C, G, T] = input[2].split(" ").map(Number);
  const dict = { A: 0, C: 0, G: 0, T: 0 };
  const possible = () => {
    return dict["A"] >= A && dict["C"] >= C && dict["G"] >= G && dict["T"] >= T;
  };
  for (let i = 0; i < P; i++) {
    dict[string[i]]++;
  }
  let res = 0;
  for (let i = 0; i <= S - P; i++) {
    if (possible()) res++;
    dict[string[i]]--;
    dict[string[i + P]]++;
  }
  console.log(res);
}

solution();
