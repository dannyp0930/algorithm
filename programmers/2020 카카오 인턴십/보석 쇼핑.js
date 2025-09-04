function solution(gems) {
    const cnt = new Set(gems).size;
    const gemsMap = new Map();
    let ans = [1, gems.length]
    let l = 0, r = 0;
    gemsMap.set(gems[0], 1);
    while (r < gems.length) {
        if (gemsMap.size === cnt) {
            if (ans[1] - ans[0] > r - l) {
                ans = [l + 1, r + 1];
            }
            gemsMap.set(gems[l], gemsMap.get(gems[l]) - 1);
            if (gemsMap.get(gems[l]) === 0) {
                gemsMap.delete(gems[l]);
            }
            l++;
        } else {
            r++;
            const exist = gemsMap.get(gems[r]);
            gemsMap.set(gems[r], exist ? exist + 1 : 1);
        }
    }
    return ans;
}