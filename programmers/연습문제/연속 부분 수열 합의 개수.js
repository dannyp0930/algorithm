function solution(elements) {
  const set = new Set();
  const arr = [...elements, ...elements];
  const n = elements.length;
  for (let i = 1; i <= n; i++) {
    for (let j = 0; j < n; j++) {
      const sum = arr.slice(j, j + i).reduce((a, b) => a + b);
      set.add(sum);
    }
  }
  return set.size;
}
