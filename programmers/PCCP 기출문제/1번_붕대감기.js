function solution(bandage, health, attacks) {
  let ans = health;
  let time = 0;
  for (let attack of attacks) {
    const cure = attack[0] - time;
    for (let i = 1; i < cure; i++) {
      ans = ans + bandage[1] > health ? health : ans + bandage[1];
      if (i % bandage[0] === 0) {
        ans += bandage[2];
      }
    }
    ans -= attack[1];
    if (ans < 0) {
      return -1;
    }
    time = attack[0];
  }
  return ans > 0 ? ans : -1;
}
