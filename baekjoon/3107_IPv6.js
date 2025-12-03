const fs = require("fs");
const str =
  process.platform === "linux"
    ? fs.readFileSync(0, "utf-8").toString().trim()
    : fs.readFileSync("input.txt").toString().trim();

function solution(str) {
  let group;
  if (str.includes("::")) {
    const [l, r] = str.split("::").map((x) => (x ? x.split(":") : []));
    const short = 8 - l.length - r.length;
    group = [...l, ...Array(short).fill("0000"), ...r];
  } else {
    group = str.split(":");
  }
  group = group.map((x) => x.padStart(4, "0"));
  console.log(group.join(":"));
}

solution(str);
