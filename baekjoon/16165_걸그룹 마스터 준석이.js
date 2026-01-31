const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim()
  .split("\n");

function solution(input) {
  const [N, M] = input[0].split(" ").map(Number);
  let idx = 1;
  let cnt = 0;
  const memToGroup = new Map();
  const groupToMem = new Map();
  for (let i = 0; i < N; i++) {
    const groupName = input[idx++];
    const memberCnt = Number(input[idx++]);
    const members = [];
    for (let j = 0; j < memberCnt; j++) {
      const member = input[idx++];
      memToGroup.set(member, groupName);
      members.push(member);
    }
    groupToMem.set(groupName, members.sort());
  }
  const res = [];
  for (let i = 0; i < M; i++) {
    const query = input[idx++];
    const type = input[idx++];
    if (type === "0") res.push(...groupToMem.get(query));
    else res.push(memToGroup.get(query));
  }
  console.log(res.join("\n"));
}

solution(input);
