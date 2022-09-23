function solution(n, works) {
  if (works.reduce((a, b) => a + b) <= n) return 0;
  let sorted = works.sort((a, b) => b - a);
  const len = works.length;
  while (n) {
      const max = sorted[0];
      for (let i = 0; i < len; i++) {
          if (sorted[i] === max) {
              sorted[i]--;
              n--;   
          }
          if (n <= 0) break;
      }
  }
  return sorted.reduce((a, b) => a + Math.pow(b, 2), 0);
}