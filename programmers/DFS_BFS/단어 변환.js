function solution(begin, target, words) {
  const n = words.length;
  visit = Array(n).fill(false);
  q = [[begin, 0]];
  while (q.length) {
    const [word, cnt] = q.shift();
    if (word === target) return cnt;
    for (let i = 0; i < n; i++) {
      if (!visit[i]) {
        let diff_cnt = 0;
        for (let j = 0; j < word.length; j++) {
          if (word[j] !== words[i][j]) {
            diff_cnt++;
          }
          if (diff_cnt > 1) break;
        }
        if (diff_cnt === 1) {
          q.push([words[i], cnt + 1]);
          visit[i] = true;
        }
      }
    }
  }
  return 0;
}
