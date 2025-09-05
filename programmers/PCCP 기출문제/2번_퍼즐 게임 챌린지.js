function solution(diffs, times, limit) {
    const n = diffs.length;
    let lo = 1, hi = 100000, answer = 100000;
    const possilbe = (level) => {
        let t = times[0];
        for (let i = 1; i < n; i++) {
            if (diffs[i] <= level) {
                t += times[i];
            } else {
                t += (diffs[i] - level) * (times[i] + times[i - 1]) + times[i];
            }
            if (t > limit) {
                return false;
            }
        }
        return true;
    }
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        if (possilbe(mid)) {
            answer = mid;
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }
    return answer;
}