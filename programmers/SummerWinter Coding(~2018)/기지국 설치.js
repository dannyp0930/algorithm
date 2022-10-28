function solution(n, stations, w) {
  let answer = 0;
  const range = 2 * w + 1;
  const l = stations.length;
  for (let i = 0; i <= l; i++) {
    const s = i == 0 ? 1 : stations[i - 1] + w + 1;
    const e = i == l ? n : stations[i] - w - 1;
    if (s <= e) {
      const length = e - s + 1;
      answer += Math.ceil(length / range);
    }
  }
  return answer;
}
