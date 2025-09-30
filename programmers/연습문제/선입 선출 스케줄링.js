function solution(n, cores) {
    const c = cores.length;
    if (n <= c) return n;
    let low = 1;
    let high = Math.max(...cores) * n;
    let time = 0;
    let work = 0;
    while (low <= high) {
        let mid = (low + high) >> 1;
        let cnt = c;
        for (const core of cores) {
            cnt += (mid / core) >> 0;
        }
        if (cnt >= n) {
            time = mid;
            work = cnt;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    work -= n;
    for (let i = c - 1; i >= 0; i--) {
        if (!(time % cores[i])) {
            if (!work) return i + 1;
            work--;
        }
    }
}