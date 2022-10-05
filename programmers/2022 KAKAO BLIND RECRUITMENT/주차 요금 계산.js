function timeToMinute(time) {
  const [h, m] = time.split(":").map((x) => parseInt(x));
  return h * 60 + m;
}

function solution(fees, records) {
  const cars = {};
  records.forEach((r) => {
    const [time, car, inOut] = r.split(" ");
    const t = timeToMinute(time);
    if (car in cars) {
      cars[car].push([t, inOut]);
    } else {
      cars[car] = [[t, inOut]];
    }
  });
  const orders = [];
  for (const [car, times] of Object.entries(cars)) {
    let t = 0;
    for (const time of times) {
      if (time[1] == "IN") {
        t -= time[0];
      } else {
        t += time[0];
      }
    }
    if (t <= 0) {
      t += 23 * 60 + 59;
    }
    orders.push([car, t]);
  }
  const ans = orders
    .sort((a, b) => a[0] - b[0])
    .map((data) => {
      let fee = fees[1];
      const t = data[1];
      if (t > fees[0]) {
        fee += Math.ceil((t - fees[0]) / fees[2]) * fees[3];
      }
      return fee;
    });
  return ans;
}
