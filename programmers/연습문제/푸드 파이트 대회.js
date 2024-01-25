function solution(food) {
  let order = "";
  food.forEach((a, i) => {
    if (!i) return;
    const cnt = parseInt(a / 2);
    order += i.toString().repeat(cnt);
  });
  return order + 0 + [...order].reverse().join("");
}
