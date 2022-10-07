function solution(n, computers) {
  function bfs(visit, i) {
    const q = [i];
    while (q.length) {
      let node = q.pop();
      visit[node] = true;
      for (let v = 0; v < n; v++) {
        if (v === node) continue;
        if (!visit[v] && computers[node][v]) {
          q.push(v);
        }
      }
    }
  }

  let ans = 0;
  const visit = Array(n).fill(false);
  for (let i = 0; i < n; i++) {
    if (visit[i] === false) {
      bfs(visit, i);
      ans += 1;
    }
  }
  return ans;
}
