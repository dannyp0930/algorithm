function solution(routes) {
  let answer = 0;
  routes.sort((a, b) => a[1] - b[1]);
  let cam_pos = -30000;
  for (const [r_s, r_e] of routes) {
    if (cam_pos < r_s) {
      cam_pos = r_e;
      answer++;
    }
  }
  return answer;
}
