function solution(name, yearning, photo) {
  const answer = [];
  const score = {};
  name.forEach((n, idx) => {
    score[n] = yearning[idx];
  });
  photo.forEach((p) => {
    answer.push(p.reduce((a, c) => a + (score[c] ?? 0), 0));
  });
  return answer;
}
