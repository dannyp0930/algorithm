function solution(info, n, m) {
    const sorted = info.sort((a, b) => b[0] / b[1] - a[0] / a[1] || b[1] - a[1]);
    const length = info.length;
    let a = 0, b = 0;
    for (let i = 0; i < length; i++) {
        if (b + sorted[i][1] >= m) {
            a += sorted[i][0];
        } else {
            b += sorted[i][1];
        }
    }
    return a >= n ? -1 : a;
}