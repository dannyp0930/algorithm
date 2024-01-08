function solution(players, callings) {
  const rank = {};
  const play = {};
  players.forEach((player, idx) => {
    rank[player] = idx;
    play[idx] = player;
  });
  callings.forEach((call) => {
    const idx = rank[call];
    const over = play[idx - 1];
    play[idx] = over;
    play[idx - 1] = call;
    rank[over] += 1;
    rank[call] -= 1;
  });
  return Object.values(play);
}
