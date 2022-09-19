function solution(operations) {
  const hq = [];
  operations.forEach(op => {
      let [command, num] = op.split(' ');
      num = parseInt(num);
      if (command == 'I') {
          hq.unshift(num);
          hq.sort((a, b) => b - a);
      } else if (hq.length > 0) {
          if (num === 1) {
              hq.shift();   
          } else {
              hq.pop();
          }
      }
  });
  if (hq.length > 0) {
      return [Math.max(...hq), Math.min(...hq)];
  }
  return [0, 0];
}