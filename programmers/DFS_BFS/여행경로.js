function solution(tickets) {
  const answer = [];
  const sortedTickets = tickets.sort((a, b) => {
    if (a[1] < b[1]) return 1;
    if (a[1] > b[1]) return -1;
    if (a[1] === b[1]) return 0;
  });
  const dict = {};
  for (const [depart, arrive] of sortedTickets) {
    if (depart in dict) {
      dict[depart].push(arrive);
    } else {
      dict[depart] = [arrive];
    }
  }
  function dfs() {
    const stack = ["ICN"];
    while (stack.length > 0) {
      const depart = stack.at(-1);
      if (depart in dict && dict[depart].length > 0) {
        const tmp = dict[depart].pop();
        stack.push(tmp);
      } else {
        const tmp = stack.pop();
        answer.push(tmp);
      }
    }
  }
  dfs();
  return answer.reverse();
}
