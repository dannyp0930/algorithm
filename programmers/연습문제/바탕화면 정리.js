function solution(wallpaper) {
  const rL = wallpaper.length;
  const cL = wallpaper[0].length;
  let r1 = rL,
    c1 = cL,
    r2 = 0,
    c2 = 0;
  wallpaper.forEach((row, r) => {
    for (let c = 0; c < cL; c++) {
      if (row[c] === "#") {
        r1 = Math.min(r1, r);
        c1 = Math.min(c1, c);
        r2 = Math.max(r2, r);
        c2 = Math.max(c2, c);
      }
    }
  });
  return [r1, c1, r2 + 1, c2 + 1];
}
