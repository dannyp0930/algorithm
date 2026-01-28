const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? 0 : "input.txt", "utf-8")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const events = input.slice(1).map((x) => x.split(" "));

function solution(N, events) {
  events.push([null, "48:00"]);
  const scores = [0, 0];
  let cur = 0;
  const times = [0, 0];
  const getSeconds = (time) => {
    const [m, s] = time.split(":").map(Number);
    return m * 60 + s;
  };
  const formatTime = (time) => {
    const m = String((time / 60) >> 0).padStart(2, "0");
    const s = String(time % 60).padStart(2, "0");
    return `${m}:${s}`;
  };
  for (let i = 0; i <= N; i++) {
    const no = events[i][0];
    const time = getSeconds(events[i][1]);
    const dur = time - cur;
    if (scores[0] > scores[1]) times[0] += dur;
    else if (scores[0] < scores[1]) times[1] += dur;
    if (no === "1") scores[0]++;
    else if (no === "2") scores[1]++;
    cur = time;
  }
  console.log(times.map(formatTime).join("\n"));
}

solution(N, events);
