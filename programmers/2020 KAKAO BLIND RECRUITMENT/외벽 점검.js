function solution(n, weak, dist) {
    const getPermutation = (cnt, candi, res, dist) => {
        if (candi.length === cnt) {
            res.push(candi.map((i) => dist[i]));
            return;
        }
        for (let j = 0; j < cnt; j++) {
            if (!candi.includes(j)) {
                getPermutation(cnt, [...candi, j], res, dist);
            }
        } 
    }
    dist.sort((a, b) => b - a);
    for (let cnt = 1; cnt <= dist.length; cnt++) {
        const permutation = [];
        getPermutation(cnt, [], permutation, dist);
        for (const perm of permutation) {
            for (let i = 0; i < weak.length; i++) {
                const converted = [...weak.slice(i), ...weak.slice(0, i).map((w) => w + n)];
                for (const p of perm) {
                    const cover = converted[0] + p;
                    while (converted[0] <= cover) {
                        converted.shift();
                    }
                    if (!converted.length) return cnt;
                }
            }
        }
    }
    return -1;
}