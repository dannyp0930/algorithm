function solution(cap, n, deliveries, pickups) {
    let answer = 0;
    let d = n - 1, p = n - 1;
    while (d >= 0 || p >= 0) {
        while (d >= 0 && !deliveries[d]) d--;
        while (p >= 0 && !pickups[p]) p--;
        answer += d > p ? 2 * (d + 1) : 2 * (p + 1);
        let dCap = cap, pCap = cap;
        while (dCap && d >= 0) {
            if (deliveries[d]) {
                deliveries[d]--;
                dCap--;
            } else {
                d--;
            }
        }
        while (pCap && p >= 0) {
            if (pickups[p]) {
                pickups[p]--;
                pCap--;
            } else {
                p--;
            }
        }
    }
    return answer;
}