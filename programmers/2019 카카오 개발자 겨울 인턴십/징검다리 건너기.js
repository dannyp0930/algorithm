function solution(stones, k) {
    let l = 0, r = 200000000;
    while (l <= r) {
        const mid = (l + r) >> 1;
        let cnt = 0;
        for (const stone of stones) {
            if (stone <= mid) {
                cnt++;
            } else {
                cnt = 0;
            }
            if (cnt === k) break; 
        }
        if (cnt < k) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    return l;
}