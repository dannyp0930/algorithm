function solution(h1, m1, s1, h2, m2, s2) {
    const getSeconds = (h, m, s) => h * 3600 + m * 60 + s;
    const getAlarm = (t) => {
        const sh = (t * 719 / 43200) >> 0;
        const sm = (t * 59 / 3600) >> 0;
        const c = (t / 43200) >> 0;
        return sh + sm - c;
    }
    const t1 = getSeconds(h1, m1, s1);
    const t2 = getSeconds(h2, m2, s2);
    let cnt = getAlarm(t2) - getAlarm(t1);
    if (!((t1 * 59) % 3600) || !((t1 * 719) % 43200)) cnt++;
    return cnt;
}
