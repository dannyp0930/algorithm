function solution(users, emoticons) {
    let ans = [0, 0];
    const discount = [];
    const calc = () => {
        let tmp = [0, 0];
        users.forEach((user) => {
            const [rate, limit] = user;
            let pay = 0;
            emoticons.forEach((emo, i) => {
                if (discount[i] >= rate) {
                    pay += emo * (100 - discount[i]) / 100;
                }
            });
            if (pay >= limit) {
                tmp[0]++;
                pay = 0;
            }
            tmp[1] += pay;
        });
        if (ans[0] < tmp[0] || (ans[0] === tmp[0] && ans[1] < tmp[1])) {
            ans = [...tmp];
        }
    }
    const dfs = (cnt) => {
        if (cnt === emoticons.length) {
            calc();
            return;
        }
        for (let i = 10; i <= 40; i += 10) {
            discount[cnt] = i;
            dfs(cnt + 1);
        }
    }
    dfs(0);
    return ans;
}